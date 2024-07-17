from asyncio.subprocess import DEVNULL
import os, json, re, csv, datetime, subprocess, sys
import string
from typing import cast
 
# Read from jsonfile
def read_json_file(filename):
   try:
      with open(filename) as json_file:
         file_content = json.load(json_file)
   except Exception as e:
      # Error reading json file
      errorMessage = "Error reading json file {}.".format(filename)
      errorMessage = "{0} Stacktrace: {1}".format(errorMessage,e)
      print(errorMessage)
      return
   return file_content
 
# Read the environment Config File, and return the config dictionary
def get_config_by_project(project_id):
   config_filename="{}/automation/config/config-{}.json".format(os.getenv('SRE'),project_id)
   if not config_filename:
      config = None
   else: 
      config = read_json_file(config_filename)
   return config
 
def convert_terminal_table_output_to_list_of_list(terminal_table_output):
   temp_list = []
   result_list = []
   # Split the lines and createa list
   temp_list = terminal_table_output.splitlines()
   # Loop through the list, and split each element by word
   for item in temp_list:
      result_list.append(item.split())
   return result_list
 
def convert_terminal_table_output_to_list_of_dictionaries(terminal_table_output):
   temp_list = []
   result_list = []
   header_dict = {}
   # Split the lines and create list
   temp_list = terminal_table_output.splitlines()
   # Loop through the list, and split each element by word, andform dictionary
   counter = 0
   for item in temp_list:
      temp_dict= {}
      if item.strip() == "":
         # Break from the forloop if item is blanks
         break
      if counter == 0:
         # Processing Header row
         inner_counter = 1
         for word in re.split(r" {2,}", item):
            header = "header{}".format(inner_counter)
            header_dict[header] = word
            inner_counter += 1
         # result_list.append(temp_dict)
      else:
         inner_counter = 1
         for word in re.split(r" {2,}", item):
            header = "header{}".format(inner_counter)
            temp_dict[header_dict[header]] = word
            inner_counter += 1
         result_list.append(temp_dict)
      counter += 1
   return result_list
 
# Return thefirst item in the list, that matches all the search criteria
# Arguments:
# 1. List of strings
# 2. Variable i.e. 1 or more Arguments Search Text string(s)
def get_first_item_in_the_list_matching_search_criteria(search_in_list,*args):
   # Initialize the response dictionary
   response = {
      "string_meeting_search_criteria": None,
      "string_meeting_search_criteria_found": False,
      "message":"Item matching ALL the search criteria NOT FOUND.",
      "validOutputReturned": True
   }
   # Validate the search_in_list contains 1 or more items
   if len(search_in_list) == 0:
      # Noitems in the search_in_list. Don't search
      return response
   # Validate that there are arguments passedin the searchlist
   if len(args) == 0:
      # No search criteria supplied
      response['validOutputReturned'] = False
      response['message'] = "Searchcriteria not provided. Cannot search. Aboring."
      return response
   # All good. Move forward with the search
   file_found = False
   for item in search_in_list:
      # Search each item for each search string passed
      if all(x in item for x in args):
         # Item meets ALLthe searchcriteria
         response['string_meeting_search_criteria'] =item
         response['message'] = "Item matching ALL the search criteria FOUND."
         response['string_meeting_search_criteria_found'] = True
         file_found = True
         break
   return response
 
# Add a field to the CSV
def add_field_to_csv(csv_file_name, field_header,field_value):
   # Initialize the response dictionary
   response = {
      "message": "CSV updated successfully.",
      "validOutputReturned": True
   }
   try:
      r = csv.reader(open(csv_file_name))
   except Exception as e:
      # Error reading the CSVfile
      errorMessage = "Error reading CSVfile {}.".format(csv_file_name)
      errorMessage = "{0} Stacktrace: {1}".format(errorMessage,e)
      response['message'] = errorMessage
      response['validOutputReturned'] = False
      return response
   # All good. Keep going.
   lines = list(r)
   lines_appended_with_the_new_field = []
   counter = 0
   for line in lines:
      if counter == 0:
         # Headerrow
         line.append(field_header)
      else:
         line.append(field_value)
      counter += 1
      # Append this LINE to linés_appended_with_the_new_field
      lines_appended_with_the_new_field.append(line)

   # Replace the csv contents with the lineés_appended_with_the_new_field
   try:
      # Open the CSVfile in Write mode
      writer = csv.writer(open(csv_file_name, 'w'))
      # Replaceall the contents of thefile with lines_appended_with_the_new_field
      writer.writerows(lines_appended_with_the_new_field)
   except Exception as e:
      # Error reading the CSVfile
      errorMessage = "Errorwriting to the CSV file {}.".format(csv_file_name)
      errorMessage = "{0} Stacktrace: {1 }".format(errorMessage,e)
      response['message'] = errorMessage
      response['validOutputReturned'] = False
      return response

   # All good. Keep going.
   return response

# Input: 08102021112908
# Output is a datetime Object
def convert_string_to_date(config,date_string):
   # Initialize the response dictionary
   response = {
      "datetime_object": None,
        "message": "",
        "validOutputReturned": True
   }
  # Validate Argument to be of exactly 14 characters
   if len(date_string) != 14:
      errorMessage = "Input date_string MUST be 14 characters."
      response['message’'] = errorMessage
      response['validOutputReturned'] = False
      return response
  # All good. Keep going.
   warningMessage = None
   try:
      month = int(date_string[0:2])
   except Exception as e:
      warningMessage = "{} Error getting MONTH value from date_string passed as argument. Setting value to 0.".format(warningMessage)
      warningMessage = "{0} Stacktrace: {1}".format(warningMessage,e)
      month = 0
   try:
      day = int(date_string[2:4])
   except Exception as e:
      warningMessage = "{} Error getting DAY value from date_string passed as argument. Setting value to 0.".format(warningMessage)
      warningMessage = "{0} Stacktrace: {1}".format(warningMessage,e)
      day =0
 
   try:
       year = int(date_string[4:8])
   except Exception as e:
      warningMessage = "{} Error getting YEAR value from date_string passed as argument. Setting value to 0.".format(warningMessage)
      warningMessage = "{0} Stacktrace: {1}".format(warningMessage,e)
      year = 0
   try:
       hour = int(date_string[8:10])
   except Exception as e:
      warningMessage = "{} Error getting HOUR value from date_String passed as argument. Setting value to 0.".format(warningMessage)
      warningMessage = "{0} Stacktrace: {1}".format(warningMessage,e)
      hour = 0
   try:
      minute = int(date_string[10:12])
   except Exception as e:
      warningMessage = "{} Error getting MINUTE value from date_string passed as argument. Setting value to 0.".format(warningMessage)
      warningMessage = "{0} Stacktrace: {1}".format(warningMessage,e)
      minute = 0
   try:
      second = int(date_string[12:14])
   except Exception as e:
      warningMessage = "{} Error getting SECOND value from date_string passed as argument. Setting value to 0.".format(warningMessage)
      warningMessage = "{0} Stacktrace: {1}".format(warningMessage,e)
      second = 0
  # Populate the message field in the response dictionary with the warningMessage
   response['message'] = warningMessage
   if config['debug_message_on']:
      print("Input Date String: {}".format(date_string))
      print("Year: {}".format(year))
      print("Month: {}".format(month))
      print("Day: {}".format(day))
      print("Hour: {}".format(hour))
      print("Minute: {}".format(minute))
      print("Second: {}".format(second))
   try:
      datetime_object = datetime.datetime(year, month, day, hour,minute,second)
   except Exception as e:
      datetime_object = datetime.datetime.now()
      waringMessage = "Error forming the datetime object from the passed date_string. Sending the default current timestamp."
      warningMessage = "{0} Stacktrace: {1}".format(warningMessage,e)
      response['message'] = warningMessage
   response['datetime_object'] = datetime_object
   return response
 
# Get the name of the resource from full GCP URL Path
# Examples below:
# Input: Network: https://www.googleapis.com/compute/v 1/projects/efx-gcp-ews-svpc-npe-6787/global/networks/ews-net-npe
# Output: ews-net-npe
# Input:projects/477100194722/regions/us-east' /instanceGroupManagers/es-uc-external-web-dev-mig
# Output: es-uc-external-web-dev-mig
def extract_name_from_gcp_path(path_url):
   gcp_resource = path_url.split('/')[-1]
   return gcp_resource
 
# Break the Machine Type URLto extract Name, Zone, CPUs and Memory
# Example:
# Input: https://www.googleapis.com/compute/v1/projects/ews-es-uc-npe-6909/zones/us-east1-b/machineTypes/n1-standard-2
# Output: ["n1-standard-2","us-east1-b"
def get_machine_type_and_zone_from_machine_type_url(machine_type_url):
   response = {
     "machine_type": "",
     "zone": ""
  }
  # Get Machine Type
   response['machine_type'] = extract_name_from_gcp_path(machine_type_url)
   # Get Machine Zone
   machine_type_url_break_list = machine_type_url.split('/')
   zone_index = machine_type_url_break_list.index("Zones") + 1
   response['zone'] = machine_type_url_break_list[zone_index]
   return response
 
# all_items_list is a list of dictionaries
# Return a subsetof all_items_list, matching key = value
def shortlist_based_on_key(all_items_list,key,value):
   subset_list = []
   for item in all_items_list:
      if item[key] == value:
          subset_list.append(item)
   return subset_list
 
def split_number_from_str(input_string):
   split_output = {
      "number_part": 0,
      "str_part": ""
   }
   str_list = []
   int_list = []
   value, unit =", "
   for item in input_string:
      try:
          item = int(item)
      except:
         # Not an integer
         str_list.append(item)
         split_output['str_part'] = ''.join(str_list)
      else:
         # Integer.
         int_list.append(str(item))
         # if you wantit to be string just do z = " join(int_list)
         split_output['number_part'] = int(''.join(int_list))
   return split_output
 
def standardize_cpu_value(cpu):
   # Convert millicores to cores
   cpu_cores = 0
   split_cpu = split_number_from_str(cpu)
   if split_cpu['str_part'] == '':
         # CPUvalue is already in cores.
         cpu_cores = float(split_cpu['number_part'])
   elif split_cpu['str_part'] == 'm':
         # CPUis in millicores. Convert to cores.
         cpu_cores = round(split_cpu['number_part'] / 1000,2)
   else:
         cpu_cores = 0
   return cpu_cores
 
def standardize_memory_value(config,memory):
  # Convert Mi/Ki to Gi
   memory_Gi = 0
   FACTOR= config['Gi_to_Mi_multiplier']
   split_memory = split_number_from_str(memory)
   if split_memory['str_part'] == 'Gi' or \
      split_memory['str_part'] == 'G'or \
         split_memory['str_part'] == 'g':
      # Memoryis in Gi. Do nothing.
      memory_Gi = split_memory['number_part']
      pass
   elif split_memory['str_part'] == 'Mi' or \
      split_memory['str_part'] == 'M'or \
         split_memory['str_part'] == 'm':
      # Memoryis in Mi. Convert to Gi.
      memory_Gi = round(split_memory['number_part'] / FACTOR,2)
   elif split_memory['str_part'] == 'Ki' or \
      split_memory['str_part'] == 'K' or \
         split_memory['str_part'] == 'k':
      # Memory is in Ki. Convert to Mi.
      memory_Gi = round(split_memory['number_part'] / FACTOR/ FACTOR, 2)
   else:
      memory_Gi = 0

   return memory_Gi
 
def query_dictionary_list(dictionary_list,value,key):
  # Query the VALUE from thelist of dictionaries DICTIONARY_LIST for
  # dictionary key key
  # OUTPUT:List of Dictionarie(s)
   response = {
      "filtered_list": [],
      "total_record_count": 0,
      "filtered_record_count": 0,
      "message": "",
      "validOutputReturned": True
   }
   try:
      response['filtered_list'] = list(filter(lambda x:x[key]==value, dictionary_list))
   except Exception as e:
      # Unhandled exception
      errorMessage = "Error querying json. Review input data."
      errorMessage = "{0} Stacktrace: {1}".format(errorMessage,e)
      response['message'] = errorMessage
      response['validOutputReturned'] = False

   # Populate the counts
   response['total_record_count'] = len(dictionary_list)
   response['filtered_record_count'] = len(response['filtered_list'])
   return response

# Refer https://sreterminal.atlassian.net/browse/CAR-73
# Adding validation to skip the warnings. Validate "kind" for every row, and process thereafter.
# Making this function generic, to be used by other similar needs
# input_list: Original ouput from kubectl command
# value: Value to be compared. Ex. "Deployment" for kubectl get deployment output...
# col: Column number to compare the value against.. this will typically be 0. Making it flexible though.
# flag: Either "include" or "exclude". 
#     include: INCLUDE the values matching 'value' in the 'col' (this is the original need)
#     exclude: EXCLUDE the values matching 'value' in the 'col' 
# Output: subset of the input_list, with all 
def get_subset_list_of_list(input_list: list,col: int,value: string,include: bool):
   response = {
      "filtered_list": [],
      "total_record_count": 0,
      "filtered_record_count": 0,
      "message": "",
      "validOutputReturned": True
   }
   try:
      for item in input_list:
         if include:
            if item[col] in (value or 'kind'):
               response['filtered_list'].append(item)
         else:
            if item[col] != value:
               response['filtered_list'].append(item)
   except Exception as e:
      # Unhandled exception
      errorMessage = "Error getting subset list of list. Review input data."
      errorMessage = "{0} Stacktrace: {1}".format(errorMessage,e)
      response['message'] = errorMessage
      response['validOutputReturned'] = False

   # Populate the counts
   response['total_record_count'] = len(input_list)
   response['filtered_record_count'] = len(response['filtered_list'])
   return response

def convert(seconds):
    seconds = seconds % (24 * 3600)
    hour = seconds // 3600
    seconds %= 3600
    minutes = seconds // 60
    seconds %= 60      
    return "%d:%02d:%02d" % (hour, minutes, seconds)

# Generate a CSV from a list of dictionaries
def write_list_of_dictionaries_to_csv(input_list_of_dictionaries,output_csv_filename):
   outputfile = open(output_csv_filename,'w+')
   output = csv.writer(outputfile)
   counter = 0
   try:
      output.writerow(input_list_of_dictionaries[0].keys())
      for row in input_list_of_dictionaries:
         counter += 1
         output.writerow(row.values())
   except IndexError:
      user_message = "No data in the input.."
   except Exception as e:
      user_message = "Error while writing to the file {}.".format(output_csv_filename)
   else:
      user_message = "{} generated.".format(output_csv_filename)
      user_message = "{}\n{} rows created.".format(user_message,counter)
   print(user_message)

def execute_bash_command(command):
   # Initialize warning check messages
   error_invalid_directory = "No such file or directory"
   # Initialize return messages
   success_message = "Command '{}' executed successfully.".format(command) # result_code 0
   error_message = "Command '{}' Failed.".format(command) # result_code 1
   warning_message = "Command '{}' returned with empty output.".format(command) # result_code 2
   # Initialize the response dictionary 
   response = {
      "result": "",
      "result_code": 0,
      "message": success_message,
      "validOutputReturned": True
   }    
   try:
      response['result'] = subprocess.getoutput(command)
   except Exception as e:
      # Command execution failed
      error_message = "{0} Stacktrace: {1}".format(error_message,e)
      response['result_code'] = 1
      response['message'] = error_message
      response['validOutputReturned'] = False
   else:
      # Command executed successfully
      if response['result'] == "":
         # Empty output.
         response['result_code'] = 2
         response['message'] = warning_message
         response['validOutputReturned'] = False
      elif error_invalid_directory in response['result']:
         response['result_code'] = 1
         response['message'] = error_invalid_directory
         response['validOutputReturned'] = False
      else:
         # All good. Default success values already set during initialization
         pass
   return response