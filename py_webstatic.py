import pickle

with open('./web_size.pickle', 'rb') as handle:
    sites = pickle.load(handle)

with open('./web_size_new.pickle', 'rb') as handle:
    sites_new = pickle.load(handle)

# Task 1
total_size = sum(site['size'] for site in sites_new)
total_size_gb = round(total_size / 1024, 2)
average_size = round(total_size / len(sites_new) / 1024, 2)

print(f"Total size is: {total_size_gb} Gb")
print(f"Avg site size is: {average_size} Gb")

# Task 2
for index in range(len(sites)):
    site_size = sites[index]['size']
    site_new_size = sites_new[index]['size']

    if site_size != site_new_size:
        difference = site_new_size - site_size
        change_rate = round((difference / (site_new_size / 100)), 2)

        print(f"{sites_new[index]['domain']} changed by: {'+' if difference > 0 else '-'}{change_rate} %")

# Task 3
empty_sites = sum(site['size'] == 0 for site in sites_new)
print(f"There are {empty_sites} empty sites")

# Task 4
for site in sites_new:
    site_size = site['size']

    if site_size > 0:
        if site_size > 1024:
            size_gb = round(site_size / 1024, 2)
            print(f"{site['domain']} is: {size_gb} Gb")
        else:
            print(f"{site['domain']} is: {site_size} Mb")


#python web static