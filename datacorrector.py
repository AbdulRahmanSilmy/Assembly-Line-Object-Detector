class data_corrector():
  '''
  A class that corrects data based on the filename and xml content
  ...

  


  Attributes
    ------------
    folderpath : str
      A string that contains the path of the folder containing both train and test images.
    
    test count: int 
      The number of errors found in the test data

    train count: int 
      The number of errors found in the train data

    test change: list
      Nested list implying the changes made to the test data. The left element is the original and the right element is the change.
    
    train change: list
      Nested list implying the changes made to the train data. The left element is the original and the right element is the change.




    Methods
    -----------
    correct()
      Carries out the correction 
  '''
  

  def __init__(self,folderpath):
    self.folderpath=folderpath
    self.test_count=0
    self.test_changes=[]
    self.train_count=0
    self.train_changes=[]

  
  def correct(self):
    print('\ncorrecting test data:')
    self.test_changes,self.test_count=self.corrector_main(self.folderpath+"/test")

    print('\ncorrecting train data:')
    self.train_changes,self.train_count=self.corrector_main(self.folderpath+"/train")

    print('\ntotal number of errors: ',self.test_count+self.train_count)

  def corrector_main(self,folderpath):
    count=0
    changes=[]
    filenames=self.xml_filenames(folderpath)
    for item in filenames:
        temp1,temp2,count=self.xml_corrector(count,item,folderpath)
        changes.append([temp1,temp2])
    print(f'{count} errors have been found')
    return changes,count

  def xml_filenames(self,folderpath):
    from os import walk
    import numpy as np 
    allfilenames = next(walk(folderpath), (None, None, []))[2] 
    filebool=[True if x.endswith('xml') else False for x in allfilenames]
    filenames=list(np.array(allfilenames)[filebool])
    return filenames

  def xml_corrector(self,count,filename,folderpath):
    xml_classes=self.classes_from_xml(filename,folderpath)
    filename_classes=self.classes_from_filename(filename)
    if len(xml_classes) != len(filename_classes):
      file_dif,xml_dif=filename_classes,xml_classes
      print(f'Filename {filename} in folder {folderpath} has unequal number of classes present in image and xml file')
      print('Manual inspection and changing of data is required')
    else:
     file_dif,xml_dif=self.discrepency(filename_classes,xml_classes)
    if file_dif!=[]:
        count=count+1
        self.xml_modifier(folderpath,filename,file_dif,xml_dif)
    return file_dif,xml_dif,count

  def classes_from_xml(self,item,folderpath):
    import xml.etree.ElementTree as ET
    import os
    file_path=os.path.join(folderpath,item)

    tree = ET.parse(file_path)
    root = tree.getroot()

    ans=[]
    for i in range(6,10):
      try:
        string=root[i][0].text
        ans.append(string)
      except IndexError:
        break
    return ans 

  

  def classes_from_filename(self,filename):
    #filename (input) has to be a string
    classes=[]
    if 'empty' in filename:
        classes.append('Empty')
    else:
        colour=self.colour_from_filename(filename)
        if 'backcover' in filename:
            classes.append(colour+' Back Cover')
        else:
            classes.append(colour+' Front Cover')
        
        if 'pcb' in filename:
            classes.append('PCB')
            if 'fuse' in filename:
                if 'rear' in filename or 'both' in filename:
                    classes.append('Rear Fuse')
                if 'top' in filename or 'both' in filename:
                    classes.append('Top Fuse')
                
    return classes

  def colour_from_filename(self,filename):
    try:
        if 'backcover' in filename:
            del_point=filename.index('backcover')
            return filename[:del_point].capitalize()
        elif 'cover' in filename:
            del_point=filename.index('cover')
            return filename[:del_point].capitalize() 
    except ValueError:
        print('filename does not contain \'backcover\' or \'cover\'')

  def comparison(self,item1,item2):
    if item1==item2:
        return False
    else:
        return True

  def discrepency(self,filename_classes,xml_classes):
    import numpy as np
    check_list= list(map(self.comparison, filename_classes,xml_classes))
    filename_dif=np.array(filename_classes)[check_list]
    xml_dif=np.array(xml_classes)[check_list]
    return list(filename_dif),list(xml_dif)

  def xml_modifier(self,folderpath,file_name,file_dif,xml_dif):
    import xml.etree.ElementTree as ET
    import os

    file_path=os.path.join(folderpath,file_name)

    tree = ET.parse(file_path)
    root = tree.getroot()
    
    for file_class,xml_class in zip(file_dif, xml_dif):
        for i in range(6,10):
            try:
                if root[i][0].text == xml_class:
                    root[i][0].text=file_class
            except IndexError:
                break
    tree.write(os.path.join(folderpath,file_name))

  