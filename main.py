import argparse
import sys
import os

from utils import show_title
from service import get_address_by_latlng
from exceptions import GmapsClientError

SIDE_QTY_MERIDIANS = 180
HEMISPHERE_QTY_PARALELS =  90


arg_parser =  argparse.ArgumentParser(prog="onde-estou-py", description="A um comando do seu endereço")

arg_parser.add_argument("--config", type=bool, dest="config", action=argparse.BooleanOptionalAction)

arg_parser.add_argument("--latitude", type=float, dest="latitude", action="store")
arg_parser.add_argument("--longitude", type=float, dest="longitude", action="store")



if __name__ == "__main__":
    show_title()

    args = arg_parser.parse_args()

    if args.config:
        gmaps_api_key = input("Informe a sua API KEY do Google Maps:  ")

        os.environ["GMAPS_API_KEY"] = gmaps_api_key.strip()

        print("Variável GMAPS_API_KEY configurada com sucesso!!")

        sys.exit(0)


    if args.longitude is None:
        print("O parametro --longitude, não pode estar com valor vazio")
        sys.exit(1)


    if args.latitude is None:
        print("O parametro --latitude, não pode estar com valor vazio")
        sys.exit(1)


    latitude =  args.latitude
    longitude = args.longitude

    if latitude < -HEMISPHERE_QTY_PARALELS  or latitude > HEMISPHERE_QTY_PARALELS:
        print("A Latitude informada é inválida")
        sys.exit(1)

    if longitude < -SIDE_QTY_MERIDIANS or longitude > SIDE_QTY_MERIDIANS:
        print("A Longitude informada é inválida")
        sys.exit(1)


    try:

        maps_api_key =  os.environ.get("GMAPS_API_KEY")

        resp = get_address_by_latlng(latitude=latitude, longitude=longitude, gmaps_apikey=maps_api_key)
        address =  resp["results"][0]

        f_address =  address["formatted_address"]

        print(f"Endereço Encontrado: {f_address}")
    except GmapsClientError as gmaps_error:
        print(gmaps_error)
        sys.exit(2)

    except RuntimeError as err:
        print(err)
        sys.exit(-1)

    sys.exit(0)
