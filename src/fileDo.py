# -*- coding: cp936 -*-
import os
import apkDo


'''
�����ļ����ļ��е�����
currentDir : �ļ���
'''
def fileTraversal(currentDir):
    files = os.listdir(currentDir)
    '''
        �˴���tempFileֻ���ļ�����
        û���ļ���·����
        ������Ҫ�ж��Ƿ��ļ��У���������ļ���·��
    '''
    print "currentDir:"+currentDir
    for tempFile in files:
        tempStr = ''
        '''����·��'''
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


