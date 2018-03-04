
# coding: utf-8

# # Search Food Vendor Status 
# 
# { name : Enter the name of desired Food Vendor}

# In[21]:


#CrossCompute
name = ''
target_folder = '/tmp'
#source_table_path = 'Fvt_Lat_Long.csv'


# In[22]:


source_table_path = 'Fvt_Lat_Long.csv'


# In[23]:


import pandas as pd
url = 'https://www.nycgovparks.org/bigapps/DPR_Eateries_001.json'
fvt = pd.read_json(url, convert_dates=['state_date', 'end_date'])


# In[24]:


selected_fvt = fvt[fvt['name'].str.contains(name, case=False)]


# In[25]:


length = len(selected_fvt)
if(length == 0):
    print("There are no matching Food Vendors with this name.")
elif(length == 1):
    print("There is %s" %length + " matching Food Vendor with this name.")
elif(length>1):
    print("There are %s" %length + " matching Food Vendors with this name")


# In[26]:


print("Vendors_with_matching_name = %s" %length)


# In[27]:


from datetime import datetime
now = datetime.now()
filtered_fvt = selected_fvt[now > selected_fvt['end_date']]
exp_len = len(filtered_fvt)
print("There are %s" %exp_len + " expired Food Vendor Permits.")


# In[28]:


print("Vendors_with_expired_license = %s" % exp_len)


# In[29]:


target_path = target_folder + '/table.csv'
filtered_fvt.to_csv(target_path, index=False)
print('Expired_Vendor_table_path = %s' % target_path)


# In[30]:


from os.path import join
from shutil import copy
target_path = join(target_folder, 'Fvt_Lat_Long.csv')
copy(source_table_path, target_path)
print('example_satellite_geotable_path = ' + target_path)


# # Vendor Status
# 
# {Vendors_with_matching_name : Total number of Food Vendors with this name: }
# {Vendors_with_expired_license : Food Vendors with this name and expired licenses: }
# 

# # Landmark Math
# 
# {example_satellite_geotable : Map Rendered from Your Geotable ? }
