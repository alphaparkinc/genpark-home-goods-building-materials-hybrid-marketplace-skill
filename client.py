class HomeGoodsBuildingMaterialsHybridMarketplaceClient:
    def calculate_heavy_freight_assembly_delivery(self, furniture_sku='MDR_QUEEN_BED_WALNUT', weight_kg=75.0, destination_cep='01310_100_SAO_PAULO'):
        freight_brl = round(85.0 + (weight_kg * 1.8), 2)
        return {
            'fulfillment_quote_id': 'mdr_flt_7721',
            'furniture_sku': furniture_sku,
            'destination_region': destination_cep,
            'bulky_heavy_freight_cost_brl': freight_brl,
            'in_room_white_glove_assembly_available': True,
            'hybrid_1p_3p_drop_ship_routed': True,
            'bulky_freight_lead_time_days': 4
        }
