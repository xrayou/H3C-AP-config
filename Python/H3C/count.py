__author__ = 'TIW'

import sys

sys.path.append(r'D:\Git\Python')

from H3C import ap_ip_in_use_pool

from H3C import mac_address

from H3C import wlan_ap_all

from H3C import wlan_ap_connection_record_all

#ac_dhcp_server_ip_in_use_list = ap_ip_in_use_pool.ac_dhcp_server_ip_in_use_list

#S2626_mac_address_list = mac_address.S2626_mac_address_list

#ac_ap_all_list = wlan_ap_all.ac_ap_all_list

#ac_ap_connection_record_all_list = wlan_ap_connection_record_all.ac_ap_connection_record_all_list

ac_dhcp_server_ip_in_use = ap_ip_in_use_pool.ac_dhcp_server_ip_in_use()

S2626_mac_address_list = mac_address.S2626_mac_address()

ac_ap_all_list = wlan_ap_all.ac_ap_all()

ac_ap_connection_record_all_list = wlan_ap_connection_record_all.ac_ap_connection_record_all()

#print(ac_dhcp_server_ip_in_use)
#print(S2626_mac_address_list)
#print(ac_ap_connection_record_all_list)
#print(ac_ap_all_list)

target_list = []

for item1 in S2626_mac_address_list:
    for item2 in ac_ap_connection_record_all_list:
        for item3 in ac_ap_all_list:
            for item4 in ac_dhcp_server_ip_in_use:
                if item1[0] == item2[0]:
                    if item2[1] == item3[3]:
                        if item4[1] == item2[0]:
                            target_list.append([item2[1], item3[0], item3[2], item1[0], item4[0], item1[3]])

for item1 in S2626_mac_address_list:
    if item1[0] == 'ffff-ffff-ffff':
        target_list.append(['No-Device', 'No-Device', 'No-Device', 'No-Device', 'No-Device', item1[3]])


target_list = sorted(target_list, key=lambda item: int(item[5][12:]))

for item in target_list:
    print(item)



