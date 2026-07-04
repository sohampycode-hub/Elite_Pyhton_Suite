import csv
import requests
from bs4 import BeautifulSoup

def scrape_quotes_pipeline(output_filename="scraped_quotes.csv"):
    """Scrapes structured quote data from a secure public sandbox site and saves it to a clean CSV."""
    # Target URL is a safe, standard public data-mining playground sandbox
    target_url = "https://quotes.toscrape.com/"
    
    # Industry standard practice: pass a realistic User-Agent header so the script acts like a standard browser
    request_headers = {
        "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/120.0.0.0 Safari/537.36"
    }
    
    print(f"[~] Connecting to target network node: {target_url}...")
    try:
        response = requests.get(target_url, headers=request_headers, timeout=10)
        
        if response.status_code != 200:
            print(f"[!] Access Denied or Endpoint Error. HTTP Status: {response.status_code}")
            return
            
        print("[+] Content streamed successfully. Parsing HTML Document Object Model...")
        # Load the raw string payload into the BeautifulSoup tree structure
        soup = BeautifulSoup(response.text, "html.parser")
        
        # Target all quote blocks inside the site structure
        quote_containers = soup.find_all("div", class_="quote")
        extracted_records = []
        
        for element in quote_containers:
            # Isolate text string nodes safely using explicit selector attributes
            text_block = element.find("span", class_="text")
            author_block = element.find("small", class_="author")
            
            if text_block and author_block:
                quote_text = text_block.get_text(strip=True)
                author_name = author_block.get_text(strip=True)
                extracted_records.append((quote_text, author_name))
                
        if not extracted_records:
            print("[!] Search complete: Found no matching CSS selectors on the webpage.")
            return
            
        print(f"[~] Extracted {len(extracted_records)} records. Formatting into localized storage file: {output_filename}...")
        
        # Write the data into a clean, structured CSV format
        with open(output_filename, mode="w", newline="", encoding="utf-8") as csv_file:
            writer = csv.writer(csv_file)
            # Provision table header column keys
            writer.writerow(["Quote Text Statement", "Author / Speaker Entity"])
            # Pour the structured data collections array into the rows
            writer.writerows(extracted_records)
            
        print(f"[X] Data Mining Successful! Asset saved cleanly inside: {output_filename}")
        
        # Display a quick structural snippet directly into the terminal console
        print("\n--- Live Data Extraction Stream Preview ---")
        for idx, (quote, author) in enumerate(extracted_records[:3], start=1):
            print(f"{idx}. \"{quote[:40]}...\" — {author}")
            
    except requests.exceptions.RequestException as error_context:
        print(f"[!] Critical Network Disruption: {error_context}")

def main():
    """Main terminal loop wrapper designed for smooth interaction within Pydroid."""
    print("=" * 45)
    # Highlight to the user that it writes out to a structured analytical format
    print("     AUTOMATED STRUCTURED WEB DATA EXTRACTOR    ")
    print("=" * 45)
    print("Target Node: https://quotes.toscrape.com/\n")
    
    input("Press Enter to initialize extraction and write to CSV...")
    scrape_quotes_pipeline()
    print("=" * 45)

if __name__ == "__main__":
    main()
