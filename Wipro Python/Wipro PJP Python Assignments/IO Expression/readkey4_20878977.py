user1_20878977=input()
user2_20878977=input()
user3_20878977=input()
user4_20878977=input()
user5_20878977=input()
userlist_20878977=[user1_20878977,user2_20878977,user3_20878977,user4_20878977,user5_20878977]
unix_20878977=input()
wintel_20878977=input()
networking_20878977=input()
helpdesk_20878977=input()
bsm_20878977=input()
stream_20878977=[unix_20878977,wintel_20878977,networking_20878977,helpdesk_20878977,bsm_20878977]
userdict_20878977={}
for key in userlist_20878977:
    for value in stream_20878977:
        userdict_20878977[key]=value
        stream_20878977.remove(value)
        break
print(userdict_20878977)