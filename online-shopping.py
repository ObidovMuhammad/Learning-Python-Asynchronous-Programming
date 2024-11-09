import asyncio
import random

# Simulated delays (in seconds)
delays = [1, 2, 3]

async def browse_products():
    print("Browsing products on the website...")
    await asyncio.sleep(random.choice(delays))
    print("Found interesting products!")

async def add_to_cart(product_name):
    print(f"Adding {product_name} to the cart...")
    await asyncio.sleep(random.choice(delays))
    print(f"{product_name} added to the cart!")

async def checkout():
    print("Proceeding to checkout...")
    await asyncio.sleep(random.choice(delays))
    print("Filled out shipping information.")

async def process_payment():
    print("Processing payment...")
    await asyncio.sleep(random.choice(delays))
    print("Payment successful!")

async def main():
    # Run browse and add to cart tasks concurrently
    await asyncio.gather(
        browse_products(),
        add_to_cart("Laptop"),
        add_to_cart("Headphones")
    )
    
    # Perform checkout and payment sequentially
    await checkout()
    await process_payment()
    print("Order completed successfully!")

# Run the main function using asyncio
asyncio.run(main())
