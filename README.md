# WebScraper-in-Python--BCC-and-IAA

Crawling through the sites and fetching data, converting formats, json.
articles from main page of BBC,
and the flights table from IAA's site.
Using Selenium lib. 

For example. fetches data on flights from Paris (Hebrew: פריס):
    {
        "חברת תעופה": "EL AL ISRAEL AIRLINES",
        "טיסה": "LY 320",
        "נוחת מ": "פריס",
        "טרמינל": "3",
        "זמן מתוכנן": "16:50",
        "תאריך": "06/04",
        "זמן עדכני": "17:15",
        "סטאטוס": "נחתה"
    },
    {
        "חברת תעופה": "AMERICAN AIRLINES",
        "טיסה": "AA 8375",
        "נוחת מ": "פריס",
        "טרמינל": "3",
        "זמן מתוכנן": "16:50",
        "תאריך": "06/04",
        "זמן עדכני": "17:15",
        "סטאטוס": "נחתה"
    }
