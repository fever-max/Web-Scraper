
def save_to_file(file_name, jobs):
    file = open(f"{file_name}.csv", "w", encoding="utf-8-sig")
    file.write("title, location, company, link,\n")

    for job in jobs:
        file.write(f"{job['title']}, {job['location']}, {job['company']}, {job['link']}\n")

    file.close()