

import apk


#axmlprinter.doParseXML('AndroidManifest.xml','_AndroidManifest.xml')


def apkWork(fileNameIn, fileNameOut) :
    if fileNameIn != None :
        buff = ""

        if ".xml" in fileNameIn:
            ap = apk.AXMLPrinter(open(fileNameIn, "rb").read())
            buff = ap.get_xml_obj().toprettyxml()
        else:
            print("Unknown file type")
            return

        if fileNameOut != None :
            fd = open(fileNameOut, "w")
            fd.write( buff )
            fd.close()
        else :
            print(buff)
    else:
        print("Use axmlprinter.py -h for command line options.")

