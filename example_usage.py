from client import HomeGoodsBuildingMaterialsHybridMarketplaceClient

def main():
    client = HomeGoodsBuildingMaterialsHybridMarketplaceClient()
    res = client.calculate_heavy_freight_assembly_delivery('MDR_MODULAR_SOFA_3SEAT', 90.0, '20040_002_RIO')
    print('Quote: ' + res['fulfillment_quote_id'] + ' for ' + res['furniture_sku'])
    print('Heavy Freight Cost: BRL ' + str(res['bulky_heavy_freight_cost_brl']) + ' (Lead Time: ' + str(res['bulky_freight_lead_time_days']) + ' days)')
    print('White-Glove Assembly: ' + str(res['in_room_white_glove_assembly_available']) + ' | Hybrid 1P/3P: ' + str(res['hybrid_1p_3p_drop_ship_routed']))

if __name__ == '__main__':
    main()
