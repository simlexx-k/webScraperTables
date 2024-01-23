from bs4 import BeautifulSoup

html = """
<div class="prd card _full">
    <a class="core" href="/ailyons-afk-111-water-dispenser-hot-and-normal-with-storage-cabinet-118096692.html">
        <div class="img-c">
            <img class="img" width="104" height="104" alt="" src="https://ke.jumia.is/unsafe/fit-in/300x300/filters:fill(white)/product/29/6690811/1.jpg?1843">
            <span class="bdg _dsct _sm">20%</span>
        </div>
        <div class="info">
            <div class="bdg-w">
                <div class="bdg _mall _xs">Official Store</div>
                <img class="_ni camp" height="16" alt="CFS" src="https://ke.jumia.is/badges/cfs/1/240x32.png?4538">
            </div>
            <h3 class="name">AILYONS AFK-111 Water Dispenser Hot And Normal With Storage Cabinet</h3>
            <p class="prc">
                <span class="curr">KSh 3,999</span>
                <span class="old">KSh 4,999</span>
            </p>
            <div class="rev">
                <div class="stars _s">
                    <div class="in" style="width: 14%;"></div>
                </div>
                (122)
            </div>
            <svg aria-label="Express Shipping" class="ic xprss" width="113" height="12">
                <use href="https://www.jumia.co.ke/assets_hy/images/i-shop-jumia.dfaf1681.svg#express"></use>
            </svg>
        </div>
    </a>
    <div class="ftr">
        <div class="stk">51 items left
            <div class="meter _s" style="background-image: linear-gradient(to right, rgb(246, 139, 30) 57.3034%, rgb(199, 199, 205) 57.3034%);"></div>
        </div>
        <form class="_w-spin" action="/cart/xhr/products/AI234PB2579AXNAFAMZ-156622155/quantity/" method="post">
            <input name="action" type="hidden" value="in">
            <button class="btn _prim -fw _sm">Add to cart</button>
            <input name="capiId" type="hidden" value="0330e8aed336a81f8db11eb5a7c67b7a_1706023598_{eventType}">
            <input name="csrfToken" type="hidden" value="9dc21419067c5d971f1b6578f6512cec">
        </form>
    </div>
</div>
"""

soup = BeautifulSoup(html, 'html.parser')

# Extracting item name
item_name = soup.find('h3', class_='name').text.strip()

# Extracting current price and old price
current_price = soup.find('span', class_='curr').text.strip()
old_price = soup.find('span', class_='old').text.strip()

# Extracting rating
rating_percentage = soup.find('div', class_='stars').find('div', class_='in')['style']
rating = int(rating_percentage.split(":")[1].split("%")[0].strip())

# Displaying the results
print(f"Item Name: {item_name}")
print(f"Current Price: {current_price}")
print(f"Old Price: {old_price}")
print(f"Rating: {rating}%")
