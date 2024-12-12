#!/usr/bin/env python
"""Django's command-line utility for administrative tasks."""
import os
import sys
from dotenv import load_dotenv
import xml.etree.ElementTree as ET

# Load environment variables
load_dotenv()

def update_xml_file(xml_path):
    # Parse the XML file
    tree = ET.parse(xml_path)
    root = tree.getroot()

    # Find the data-source element
    data_source = root.find('.//data-source')

    if data_source is None:
        print("Data source element not found in XML file")
        return

    jdbc_url = f"jdbc:postgresql://{os.getenv('DB_HOST')}:{os.getenv('DB_PORT')}/{os.getenv('DB_NAME')}"
    data_source.find('jdbc-url').text = jdbc_url

    # Update other elements if needed
    data_source.find('driver-ref').text = os.getenv('DB_DRIVER', 'postgresql')
    data_source.find('jdbc-driver').text = os.getenv('DB_JDBC_DRIVER', 'org.postgresql.Driver')

    # Write the updated XML back to the file
    tree.write(xml_path)

def main():
    """Run administrative tasks."""
    os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'leonidas.settings')
    
    # Update XML file before executing management commands
    xml_path = './.idea/dataSources.xml'
    update_xml_file(xml_path)

    try:
        from django.core.management import execute_from_command_line
    except ImportError as exc:
        raise ImportError(
            "Couldn't import Django. Are you sure it's installed and "
            "available on your PYTHONPATH environment variable? Did you "
            "forget to activate a virtual environment?"
        ) from exc
    execute_from_command_line(sys.argv)

if __name__ == '__main__':
    main()
