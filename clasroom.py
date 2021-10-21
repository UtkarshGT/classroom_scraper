# imports
from bs4 import BeautifulSoup as soup

# data
classroom_filename = 'classroom_data.html'
final_csv_name = 'classroom_data.csv'
scrape_links = ['youtu.be']

# Final file with data
final_csv = open(final_csv_name, 'w')
final_csv.write('date, name, links\n')

# classroom html file
with open(classroom_filename) as html_file:
    html_soup = soup(html_file.read(), 'lxml')

# All posts
containers = html_soup.findAll('div', {'class': 'qhnNic LBlAUc Aopndd TIunU'})

# Collect data and write
for container in containers:
    # Find data
    date = container.find(
        'span', {'class': 'IMvYId dDKhVc YVvGBb'}).span.text[8:]
    name = container.find('span', {'class': 'YVvGBb asQXV'}).text
    links = container.findAll('a')

    # Collect links
    link_text = ''
    for link in links:
        if scrape_links in link.text:
            link_text += link.text + ' | '

    # If no link, skip current post
    if link_text == '':
        continue

    # Write row to file
    final_csv.write(date + ',' + name + ',' + link_text)
    final_csv.write('\n')

# Close file
final_csv.close()
