""" This package consist of some of  the list related function"""
import logging


class List_function:
    import logging
    logging.basicConfig(filename="log_file_for_list.log",level=logging.DEBUG,format="%(asctime)s %(levelname)s %(message)s")

    def __init__(self,lst):
        self.lst=lst

    def is_list(self):
        """Return true if given input is list,false otherwise"""
        try:
            if type(self.lst)==list:
                logging.info("The given input: {} is a list ".format(self.lst))
                return 1
            else:
                logging.info("The given input:(  {} ) is not a list".format(self.lst))
                return 0

        except Exception as e:
            logging.error("Error has occured")
            logging.exception("Exception occured" + str(e))

    def Insert_at_index(self,index,object):
        """THis function will insert the given object at given index"""
        try:
            if self.is_list():
                new_list=self.lst[:index] + [object] + self.lst[index:]
                logging.info("This is sucessfully executed and the new list is {}".format(new_list))
        except Exception as e:
            logging.exception("some Exception occured  {}".format(e))

    def Index(self, element, start=None, end=None):
        """ This function searches for a given element from the start of the list and
        returns the lowest index where the element appears. """
        if self.is_list():
            try:
                if start != None and end == None:
                    for i in range(start, len(self.lst)):
                        if self.lst[i] == element:
                            logging.info("Element {} found at index: {} ".format(element,i))
                            return i
                            break
                        else:
                            logging.info("Element {} not found in range {} to {} ".format(element,start,len(self.lst)))
                elif start != None and end != None:
                    for i in range(start, end):
                        if self.lst[i] == element:
                            logging.info("Element {} found at index: {} ".format(element,i))
                            return i
                            break
                        else:
                            logging.info("Element {} not found in range {} to {} ".format(element,start,end))
                else:
                    for i in range(0, len(self.lst)):
                        if self.lst[i] == element:
                            logging.info("Element {} found at index: {} ".format(element,i))
                            return i
                            break
                    else:
                            logging.info("Element {} not found in the list ".format(element))

            except Exception as e:
                logging.exception("some error occured"+str(e))


    def count_element(self,element):
        """This method will return the count of given element in list"""
        try:
            count=0
            for i in range(len(self.lst)):
                if self.lst[i]==element:
                    count+=1
            logging.info("Element {} is repeated {} times is given list".format(element,count))
            return count
        except Exception as e:
            logging.exception("some error occured "+ str(e))


    def append_element(self,element):
        """This method will add the given element at the  end of the list"""
        try:
            self.lst=self.lst+[element]
            logging.info("Element {} is sucessfully appended in list".format(element))
            return self.lst
        except Exception as e:
            logging.exception("some error occured "+ str(e))

    def sort_element(self,reverse=False):
        """ This will return sorted list"""
        try:
            if reverse==False:
                    for j in range(len(self.lst) - 1):
                        for i in range(len(self.lst) - 1):
                            if self.lst[i] > self.lst[i + 1]:
                                self.lst[i], self.lst[i + 1] = self.lst[i + 1], self.lst[i]
                    logging.info("Element is sucessfully sorted in ascending order and sorted list is : {}".format(self.lst))
                    return self.lst
            else:
                for j in range(len(self.lst) - 1):
                    for i in range(len(self.lst) - 1):
                        if self.lst[i] < self.lst[i + 1]:
                            self.lst[i], self.lst[i + 1] = self.lst[i + 1], self.lst[i]
                logging.info("Element is sucessfully sorted in decending order and sorted list is : {}".format(self.lst))
                return self.lst
        except Exception as e:
            logging.error("Some error occured"+ str(e))





x=List_function([9,3,6,4,9,1])
c=x.Index(4)






