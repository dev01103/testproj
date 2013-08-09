import os
import re

import config




class serverPath:
  me=None
  S='/'
  @staticmethod
  def getMe():
   if serverPath.me==None:
     serverPath.me=serverPath()
   return serverPath.me
  
  def prepServerData(self):
      self.env=os.environ
      self.fsroot_raw=__file__
      self.fsroot=self.fsroot_raw #later on
      self.url_root=''
      if self.env.has_key('HTTP_REFERER'):
       self.url_root=self.env['HTTP_REFERER']
      else:
          wd=self.env['REQUEST_URI']
          wd=re.sub(r'/cgi-bin/.*',r'',wd)
          url='http://'+self.env['HTTP_HOST']+wd+'/' # just a temporary workaround
          self.url_root=url
      
  
  def getWebUrlRoot(self):
      return self.getUrlRoot()+config.web_root
  
  def getUrlRoot(self):
      return self.url_root
  
  def getUrlCgiRoot(self):
      return self.getUrlRoot()+'cgi-bin'
  
  def __init__(self):
      self.prepServerData()