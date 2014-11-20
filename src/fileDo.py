# -*- coding: cp936 -*-
import os
import apkDo


'''
遍历文件或文件夹的内容
currentDir : 文件夹
'''
def fileTraversal(currentDir):
    files = os.listdir(currentDir)
    '''
        此处的tempFile只是文件名，
        没有文件的路径，
        所以如要判断是否文件夹，必须加上文件夹路径
    '''
    print "currentDir:"+currentDir
    for tempFile in files:
        tempStr = ''
        '''绝对路径'''
        absolutePath = os.path.join(currentDir,tempFile)
        print "absolutePath:"+absolutePath
        if os.path.isdir(absolutePath):
            tempStr = ' is dir';
            #print "currentDir1:"+currentDir
            if tempFile != 'assets':
                fileTraversal(absolutePath)
        else:
            tempStr = ' is file'
            fileType = os.path.splitext(tempFile)[1]
            if fileType == '.xml':
                if tempFile.startswith('_'):
                    print 'is Ex'
                else:
                    apkDo.apkWork(absolutePath, os.path.join(currentDir,'_'+tempFile))
                    print "currentDir2:"+currentDir
                    print 'xml file'
        #print absolutePath + tempStr

if __name__ == "__main__" :
    currentDir = os.getcwd()
    fileTraversal(currentDir)


