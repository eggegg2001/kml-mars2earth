#!/usr/bin/env python 
# -*- coding: utf8 -*- 

from xml.sax import *
import io
import re
import zipfile
import shutil
import os
import sys
import codecs
import eviltransform

reload(sys)
sys.setdefaultencoding('utf-8')

source_name = sys.argv[1]

target_name = source_name[0:len(source_name)-4] + "_converted" + source_name[len(source_name)-4:]

class OffsetHandler(ContentHandler):
    
    temp=""
    #coordinates = []
    file_writer = None
    level = 0
    #only contains \t \n and space
    all_sep_pattern = re.compile(r"^[\t\n ]+$")
    sep_pattern = re.compile(r"[\n\t ]+")

    def setFileWriter(self,filewriter):
        print("setFileWriter")
        self.file_writer = filewriter

    def startDocument(self):
        print("startDocument")
        self.file_writer.write('<?xml version="1.0" encoding="UTF-8"?>\n')

    def endDocument(self):
        print("end xml document")
    
    def startElement(self,name,attrs):
        toWrite = ""
        index = 0
        
        while index < self.level:
            toWrite += "\t"
            index += 1
            
        self.level += 1

        toWrite += "<" + name
        
        for name in attrs.getNames():
            toWrite += " " + name + "=\"" + attrs.getValue(name) + "\""

        toWrite += ">\n"
        
        self.file_writer.write(toWrite)
        self.temp=""

    def endElement(self,name):
        if name=="coordinates":
            splitArray = re.split(self.sep_pattern,self.temp)
            self.temp = ""
            
            index = 0
            while index < len(splitArray):
                if splitArray[index] != "" and splitArray[index] != "\n":
                    #self.coordinates.append(splitArray[index])
                    coordinateArray = splitArray[index].split(",")
                    if len(coordinateArray) > 2:
                        oldLog = float(coordinateArray[0])
                        oldLat = float(coordinateArray[1])
                        lat,log = eviltransform.gcj2wgs_exact(oldLat,oldLog)
                        print(lat,log)

                        if log != None:
                            coordinateArray[0] = "%r" % log
                        if lat != None:
                            coordinateArray[1] = "%r" % lat 
                        i = 0
                        temp = ""
                        while i < len(coordinateArray):
                            if temp != "":
                                temp += ","
                            temp += "%s" % coordinateArray[i]
                            i += 1
                        if self.temp != "":
                            self.temp += " "
                        self.temp += temp
                    
                index += 1
            
        index = 0
        tabs = ""

        while index < self.level-1:
            tabs += "\t"
            index += 1

        self.level -= 1

        if "<" in self.temp or "&" in self.temp:
            self.temp = "<![CDATA[" + self.temp + "]]>"
        if self.all_sep_pattern.match(self.temp):
            toWrite = ""
        else:
            toWrite = tabs + "\t" + self.temp + "\n"
            
        toWrite += tabs + "</" + name + ">\n"
        self.file_writer.write(toWrite)
        self.temp = ""

    def characters(self,content):
        self.temp+=content

    @staticmethod
    def parseFile(filename):
        print("===============START===============")
        parser = make_parser()
        handler = OffsetHandler()

        if not os.path.isfile(filename):
            print("$WARRING:%r is not a file@"  % filename)
            return
        if filename[-3:] == "kml":
            with codecs.open(target_name, mode="w", encoding="utf8") as file_writer:
                handler.setFileWriter(file_writer)
                parser.setContentHandler(handler)
                data=""
                with codecs.open(source_name, encoding="utf8") as file:
                    data = file.read().strip()
                    file.close()
                parser.parse(io.StringIO(data))
                file_writer.close()
        else:
            print("$WARRING:It's not a kml file!")
            return
        
        print("===============Success!===============")
        print("Success!Result have output into:%s" % target_name)
        print("===============Success!===============")

OffsetHandler.parseFile(source_name)
