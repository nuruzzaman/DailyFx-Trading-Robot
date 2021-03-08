# DailyFx-Trading-Robot
Financial Trading Robot

# Steps for Installation: 
We have installed ZeroMQ with python >3.6 in the Windows 10 environment. The following libraries are required in this project. 
1. Install the following libraries using- “pip”.
	- pyzmq
	- pandas
	- ipython
    -  bs4
2. Download and unzip mql-zmq-master.zip  from Github repository: (https://github.com/darwinex/dwx-zeromq-connector)
3. Copy the contents of mql-zmq-master/Include/Mql and mql-zmq-master/Include/Zmq into MT4 installation's MQL4/Include directory as-is. Your MQL4/Include directory should now have two additional folders "Mql" and "Zmq".
4. In MT4, select Tools→ Options. Enable “Allow automated trading” and “Allow DLL imports”.
5. Copy libsodium.dll and libzmq.dll from mql-zmq-master/Library/MT4 to MT4 installation's MQL4/Libraries directory.
6. Download DWX_ZeroMQ_Server_v2.0.1_RC8.mq4 and place it inside MT4 installation's MQL4/Experts directory.
7. In the Expert Advisor menu, Select the EA- DWX_ZeroMQ_Server_v2.0.1_RC8 and Modify. It will open in MetaEditor. Press Compile to check if there is any error.
8. Restart the MT4.
9. Open your command prompt and change the folder directory to “dwx-zeromq-connector-master/v2.0.1 / python / api /” folder and type “ipython”
10. Type “from DWX_ZeroMQ_Connector_v2_0_1_RC8 import DWX_ZeroMQ_Connector” command.
11. Type “_zmq = DWX_ZeroMQ_Connector()”
12. _zmq._DWX_MTX_GET_ACCOUNT_HISTORY_()
13. _zmq._DWX_MTX_GET_ALL_OPEN_TRADES_()

_mt
=DWX_MT_TO_PYTHON(_verbose=True,_type='normal',_filename='C:\workspace-FX\DailyFx-Trading-Robot\result\\test.csv')DWX_MT_TO_PYTHON(_verbose=False,_type='normal',_filename='C:\workspace-FX\DailyFx-Trading-Robot\result\\test.csv')
