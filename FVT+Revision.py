
# coding: utf-8

# # Search Food Vendor Status 
# 
# { name : Enter the name of desired Food Vendor}

# In[35]:


#CrossCompute
name = ''
target_folder = '/tmp'


# In[36]:


import pandas as pd
url = 'https://www.nycgovparks.org/bigapps/DPR_Eateries_001.json'
fvt = pd.read_json(url, convert_dates=['state_date', 'end_date'])


# In[37]:


selected_fvt = fvt[fvt['name'].str.contains(name, case=False)]
#selected_fvt[:249]


# In[38]:


length = len(selected_fvt)
if(length == 0):
    print("There are no matching Food Vendors with this name.")
elif(length == 1):
    print("There is %s" %length + " matching Food Vendor with this name.")
elif(length>1):
    print("There are %s" %length + " matching Food Vendors with this name")


# In[39]:


print("Vendors_with_matching_name = %s" %length)


# In[40]:


#gives table of the expired vendor you searched.
#Some vendors have multiple trucks so that's why a table is needed to list them and their approx location
from datetime import datetime
now = datetime.now()
filtered_fvt = selected_fvt[now > selected_fvt['end_date']]
exp_len = len(filtered_fvt)
if (exp_len>1):
    print("There are %s" %exp_len + " expired Food Vendor Permits.")
elif(exp_len==1):
    print("There is 1 expired Food Vendor Permit with this name.")
elif(exp_len==0):
    print("There are no expired Food Vendor Permits with this name.")
filtered_fvt[['name','location','park_id', 'end_date'][:249]]


# In[41]:


print("Vendors_with_expired_license = %s" % exp_len)


# In[44]:


target_path = target_folder + '/table.csv'
filtered_fvt.to_csv(target_path, index=False)
print('Expired_Vendor_table_path = %s' % target_path)


# # Vendor Status
# 
# {Vendors_with_matching_name : Total number of Food Vendors with this name: }
# {Vendors_with_expired_license : Food Vendors with this name and expired licenses: }
