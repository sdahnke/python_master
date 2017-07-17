import re

test_text = "716\u200977\u200994#w1wkg"
if re.match("([0-9]{3})\\u2009([0-9]{2})\\u2009([0-9]{2})#w1wkg", test_text):
    search = re.search("([0-9]{3})\\u2009([0-9]{2})\\u2009([0-9]{2})#w1wkg", test_text)

    print(search.group(1))
    print(search.group(2))
    print(search.group(3))

    if re.match("([0-9]{3})\\u2009([0-9]{2})\\u2009([0-9]{2})#w1wkg", str(cols)):
        search = re.search("([0-9]{3})\\u2009([0-9]{2})\\u2009([0-9]{2})#w1wkg", cols)
        cols = search.group(1) + "." + search.group(2) + "." + search.group(3)
        print(cols)
    else:
        cols = cols
    if re.match("€\xa0([0-9,]+)", str(cols)):
        search = re.search("€\xa0([0-9,]+)", cols)
        cols = search.group(1)
        print(cols)
    else:
        cols = cols



cols = row.find_all('td')
    print(cols)
    for ele in cols:
        cols = ele.text.strip()
        if re.match("([0-9]{3}).([0-9]{2}).([0-9]{2})#w1wkg", str(cols)):
            search = re.search("([0-9]{3}).([0-9]{2}).([0-9]{2})#w1wkg", cols)
            cols = search.group(1) + "." + search.group(2) + "." + search.group(3)
        if re.match("[^0-9]+([0-9,]+)", str(cols)):
            search = re.search("[^0-9]+([0-9,]+)", cols)
            cols = search.group(1)
        new_row = [ele for ele in cols if ele]
        if re.match("\[\'[0-9]+\'.*", str(new_row)):
            data.append(new_row)
            print(data)

or row in rows:
cells = row.find_all('td')
for cell in cells:
    cell = str(cell.text.strip())
    if re.match("([0-9]{3}).([0-9]{2}).([0-9]{2})#w1wkg", cell):
        search = re.search("([0-9]{3}).([0-9]{2}).([0-9]{2})#w1wkg", cell)
        cell = search.group(1) + "." + search.group(2) + "." + search.group(3)
    if re.match("[^0-9]+([0-9,]+)", cell):
        search = re.search("[^0-9]+([0-9,]+)", cell)
        cell = search.group(1)
    basket_products.append(cell)
if re.match("\[\'[0-9]+\',.*", str(basket_products)):
    print(str(basket_products))
    basket.append(basket)
basket_products = []

print(basket)
