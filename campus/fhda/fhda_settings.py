# MyPortal endpoint
SSB_ROOT_URL = 'https://ssb-prod.ec.fhda.edu'
SSB_URL = 'https://ssb-prod.ec.fhda.edu/PROD/'

# Regexes
COURSE_NAME_PATTERN = r'[FD]0*(\d+\w*)\.?'

# Available Campuses - Foothill, De Anza, and test
CAMPUS_LIST = {'fh': '202121', 'da': '202122', 'test': 'test'}

'''
Course Type Flags - Foothill College

Online   - online, fully asynchronous classes (no live meetings)
Virtual  - online, fully synchronous classes (only live meetings)
Hybrid   - online, hybrid (mixed) between `online` and `virtual` [COVID-19]
Standard - physical classes (or all of the above are N/A, e.g. "Independent Study")

Last Verified / Updated for: Fall 2020
'''
FH_TYPE_ALIAS = {'standard': None, 'online': 'W', 'virtual': 'V', 'hybrid': 'Z'}

'''
Course Type Flags - De Anza College

Online   - online, fully asynchronous classes (no live meetings)
Hybrid   - hybrid classes that are both online and physical
Standard - physical classes (or all of the above are N/A, e.g. "Independent Study")

Last Verified / Updated for: Fall 2020
'''
DA_TYPE_ALIAS = {'standard': None, 'online': 'Z', 'hybrid': 'Y'}

# Scraped table headers (for scrape_term.py)
HEADERS = (
    'raw_course',
    'CRN',
    'desc',
    'status',
    'days',
    'time',
    'start',
    'end',
    'room',
    'campus',
    'units',
    'instructor',
    'seats',
    'wait_seats',
    'wait_cap'
)

# Mapping of campuses to class type variants
# NOTE: test database currently has Foothill College data
COURSE_TYPES_TO_FLAGS = {
    'fh': FH_TYPE_ALIAS,
    'da': DA_TYPE_ALIAS,
    # 'test': FH_TYPE_ALIAS
}