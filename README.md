# linac
#============================================================
#Initialization Start
#The script within Initialization Start and Initialization End is needed for properly
#initializing Command Interface for CONEX-CC instrument.
#The user should copy this code as is and specify correct paths here.
import sys

#Command Interface DLL can be found here.
# print(sys.path,'\n')
print ("\n Adding location of Newport.CONEXCC.CommandInterface.dll to sys.path")
sys.path.append(r'C:\Windows\Microsoft.NET\assembly\GAC_64\Newport.CONEXCC.CommandInterface\v4.0_2.0.0.3__aab368c79b10b8be')
# print(sys.path,'\n')

# The CLR module provide functions for interacting with the underlying
# .NET runtime
import clr
# # Add reference to assembly and import names from namespace
# clr.AddReference("C:\\Windows\\Microsoft.NET\\assembly\\GAC_64\\Newport.CONEXCC.CommandInterface\\v4.0_2.0.0.3__aab368c79b10b8be\\Newport.CONEXCC.CommandInterface.dll")
clr.AddReference("Newport.CONEXCC.CommandInterface")

import CommandInterfaceConexCC as ccc
print(dir(ccc))
# import Newport.CONEXCC as npcc
# import Newport as npt
import System
from inspect import getmembers
# print('npt',getmembers(ccc),'\n')

print("contents")
dll_ref = System.Reflection.Assembly.LoadFile("C:\\Windows\\Microsoft.NET\\assembly\\GAC_64\\Newport.CONEXCC.CommandInterface\\v4.0_2.0.0.3__aab368c79b10b8be\\Newport.CONEXCC.CommandInterface.dll")
print('fn',dll_ref.FullName)
print('loc',dll_ref.Location)
print('def',len(dll_ref.DefinedTypes))
# for i in range(len(dll_ref.DefinedTypes)):
#     print(dll_ref.DefinedTypes[i])
# #============================================================
# # Instrument Initialization
# # The key should have double slashes since
# # (one of them is escape character)
instrumentKey="COM3"
print ('Instrument Key=>', instrumentKey)
# # create a device instance and open communication with the instrument
CC = ccc.ConexCC()
ret = CC.OpenInstrument(instrumentKey)
print ('OpenInstrument => ', ret)
# Get positive software limit
result, response, errString = CC.SR_Get(1)
if result == 0 :
    print ('positive software limit=>', response)
else:
    print ('Error=>',errString)
# Get negative software limit
result, response, errString = CC.SL_Get(1)
if result == 0 :
    print ('negative software limit=>', response)
else:
    print ('Error=>',errString)
# Get controller revision information
result, response, errString = CC.VE(1)
if result == 0 :
    print ('controller revision=>', response)
else:
    print ('Error=>',errString)
# Get current position
result, response, errString = CC.TP(1)
if result == 0 :
    print ('position=>', response)
else:
    print ('Error=>',errString)
# Unregister device
CC.CloseInstrument();
