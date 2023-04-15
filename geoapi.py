"""GEOAPI"""

import beautiful_soup
import request_module
import jsons

response = request_module.get__(
    "https://es.wikipedia.org/wiki/Anexo:Pa%C3%ADses")

soup = beautiful_soup.obtain_html(response)

table = beautiful_soup.find(soup, "table")

body = beautiful_soup.find_all(table, "tr")

info: dict = {
    "countries": []
}

IT = 1
FLAG = True

for row in body:

    flag_url = beautiful_soup.find_all(row, "img")
    for item in flag_url:
        srcset = beautiful_soup.get_attribute(item, "srcset").split(",")[1]

        if FLAG:
            info["countries"].append({
                "id": IT,
                "url_img": srcset.replace("//", "").replace("2x", "").strip()
            })
            IT += 1
            FLAG = False
    FLAG = True

j = 0

for row in body:
    list_td = beautiful_soup.find_all(row, "td")
    i = 0
    for td in list_td:
        if i == 0:
            info["countries"][j]["name"] = str(
                beautiful_soup.get_text(td)).strip()
        elif i == 1:
            info["countries"][j]["short_name"] = str(
                beautiful_soup.get_text(td)).strip()
        elif i == 4:
            info["countries"][j]["continent"] = str(
                beautiful_soup.get_text(td)).strip()
        i += 1
    if len(list_td) != 0:
        j += 1


jsons.save_json("geoapi.json", mode="w", info=info)
