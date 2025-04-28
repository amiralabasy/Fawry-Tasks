'''Task3:

List '.log' files in a directory './logs'

Output: 
    ['access.log', 'error.log']'''
########################################################################################################
import os
log_dir = './logs'
log_files = [f for f in os.listdir(r'C:\Users\Hp\Desktop\Day 2') if f.endswith('.py')]
print(log_files)