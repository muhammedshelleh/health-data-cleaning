import pandas as pd

occurrence = pd.read_csv('occurrence.csv')
occurrence.head()
dead = pd.read_csv('dead.csv')
dead.head()
factor = pd.read_csv('factor.csv')
factor.head()
combo = pd.merge(occurrence, dead, how='outer')
combo = pd.merge(combo, factor, how='outer')
combo.head()
combo.isna().sum()
who_region = {}

# African Regions
afri = "Algeria, Angola, Cabo Verde, Eswatini, Sao Tome and Principe, Benin, South Sudan, Western Sahara, Congo (Brazzaville), Congo (Kinshasa), Cote d'Ivoire, Botswana, Burkina Faso, Burundi, Cameroon, Cape Verde, Central African Republic, Chad, Comoros, Ivory Coast, Côte d'Ivoire, Democratic Republic of the Congo, Equatorial Guinea, Eritrea, Ethiopia, Gabon, Gambia, Ghana, Guinea, Guinea-Bissau, Kenya, Lesotho, Liberia, Madagascar, Malawi, Mali, Mauritania, Mauritius, Mozambique, Namibia, Niger, Nigeria, Republic of the Congo, Rwanda, São Tomé and Príncipe, Senegal, Seychelles, Sierra Leone, Somalia, South Africa, Swaziland, Togo, Uganda, Tanzania, United Republic of Tanzania, Zambia, Zimbabwe"
afri = [i.strip() for i in afri.split(',')]
for i in afri:
    who_region[i] = 'Africa'
    
#North/South American Regions
amer = 'Antigua and Barbuda, Argentina, Bahamas, Barbados, Belize, Bolivia, Bolivia (Plurinational State of), Brazil, Canada, Chile, Colombia, Congo, Costa Rica, Cuba, Dominica, Dominican Republic, Ecuador, El Salvador, Grenada, Guatemala, Guyana, Haiti, Honduras, Jamaica, Mexico, Nicaragua, Panama, Paraguay, Peru, Saint Kitts and Nevis, Saint Lucia, Saint Vincent and the Grenadines, Suriname, Trinidad and Tobago, United States, US, United States of America, Uruguay, Venezuela, Venezuela (Bolivarian Republic of)'
amer = [i.strip() for i in amer.split(',')]
for i in amer:
    who_region[i] = 'Americas'

# South-East Asia Regions
soeaas = 'Bangladesh, Bhutan, India, Indonesia, Maldives, Myanmar, Burma, Nepal, Sri Lanka, Thailand, Timor-Leste'
soeaas = [i.strip() for i in soeaas.split(',')]
for i in soeaas:
    who_region[i] = 'South-East Asia'

# european Regions
eure = 'Albania, Andorra, Greenland, Kosovo, Holy See, Liechtenstein, Armenia, Czechia, Austria, Azerbaijan, Belarus, Belgium, Bosnia and Herzegovina, Bulgaria, Croatia, Cyprus, Czech Republic, Denmark, Estonia, Finland, France, Georgia, Germany, Greece, Hungary, Iceland, Ireland, Israel, Italy, Kazakhstan, Kyrgyzstan, Latvia, Lithuania, Luxembourg, Malta, Monaco, Montenegro, Netherlands, North Macedonia, Republic of North Macedonia, Norway, Poland, Portugal, Moldova, Republic of Moldova, Romania, Russia, Russian Federation, San Marino, Serbia, Slovakia, Slovenia, Spain, Sweden, Switzerland, Tajikistan, Turkey, Turkmenistan, Ukraine, United Kingdom, United Kingdom of Great Britain and Northern Ireland, Uzbekistan, The former state union Serbia and Montenegro'
eure = [i.strip() for i in eure.split(',')]
for i in eure:
    who_region[i] = 'eurepe'

# Eastern Mediterranean Regions
eame = 'Afghanistan, Bahrain, Djibouti, Egypt, Iran, Iran (Islamic Republic of), Iraq, Jordan, Kuwait, Lebanon, Libya, Morocco, Oman, Pakistan, Palestine, West Bank and Gaza, Qatar, Saudi Arabia, Somalia, Sudan, Syria, Syrian Arab Republic, Tunisia, United Arab Emirates, Yemen'
eame = [i.strip() for i in eame.split(',')]
for i in eame:
    who_region[i] = 'Eastern Mediterranean'

# Western Pacific Regions
wepa = "Australia, Brunei, Brunei Darussalam, Republic of Korea, Cambodia, China, Cook Islands, Fiji, Japan, Kiribati, Laos, Lao People's Democratic Republic, Malaysia, Marshall Islands, Micronesia, Micronesia (Federated States of), Mongolia, Nauru, North Korea, New Zealand, Niue, Palau, Papua New Guinea, Philippines, South Korea, Democratic People's Republic of Korea, Samoa, Singapore, Solomon Islands, Taiwan, Taiwan*, Tonga, Tuvalu, Vanuatu, Vietnam, Viet Nam"
wepa = [i.strip() for i in wepa.split(',')]
for i in wepa:
    who_region[i] = 'Western Pacific'
combo['WHO Region'] = combo['Country'].map(who_region)
combo.head()
combo[combo['WHO Region'].isna()]['Country'].unique()
combo.to_csv('combo.csv', index=False)