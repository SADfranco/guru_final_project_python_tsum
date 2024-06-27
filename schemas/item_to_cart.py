add_to_cart = {
    "$schema": "http://json-schema.org/draft-04/schema#",
    "type": "object",
    "properties": {
        "items": {
            "type": "array",
            "items": [
                {
                    "type": "object",
                    "properties": {
                        "position_id": {
                            "type": "integer"
                        },
                        "item_type": {
                            "type": "string"
                        },
                        "item_id": {
                            "type": "integer"
                        },
                        "price": {
                            "type": "integer"
                        },
                        "color": {
                            "type": "object",
                            "properties": {
                                "id": {
                                    "type": "integer"
                                },
                                "title": {
                                    "type": "string"
                                },
                                "hex": {
                                    "type": "string"
                                },
                                "feminine": {
                                    "type": "string"
                                },
                                "neutral": {
                                    "type": "string"
                                },
                                "plural": {
                                    "type": "string"
                                },
                                "parental": {
                                    "type": "string"
                                },
                                "imageUrl": {
                                    "type": "null"
                                },
                                "slug": {
                                    "type": "string"
                                }
                            },
                            "required": [
                                "id",
                                "title",
                                "hex",
                                "feminine",
                                "neutral",
                                "plural",
                                "parental",
                                "imageUrl",
                                "slug"
                            ]
                        },
                        "photos": {
                            "type": "array",
                            "items": [
                                {
                                    "type": "object",
                                    "properties": {
                                        "tiny": {
                                            "type": "string"
                                        },
                                        "small": {
                                            "type": "string"
                                        },
                                        "middle": {
                                            "type": "string"
                                        }
                                    },
                                    "required": [
                                        "tiny",
                                        "small",
                                        "middle"
                                    ]
                                },
                            ]
                        },
                        "title": {
                            "type": "string"
                        },
                        "slug": {
                            "type": "string"
                        },
                        "description_lit": {
                            "type": "string"
                        },
                        "sku": {
                            "type": "object",
                            "properties": {
                                "id": {
                                    "type": "integer"
                                },
                                "content_id": {
                                    "type": "string"
                                },
                                "item_id": {
                                    "type": "integer"
                                },
                                "ext_id": {
                                    "type": "integer"
                                },
                                "ext_guid": {
                                    "type": "string"
                                },
                                "barcode": {
                                    "type": "string"
                                },
                                "barcode_vnd": {
                                    "type": "string"
                                },
                                "season": {
                                    "type": "string"
                                },
                                "size_id": {
                                    "type": "integer"
                                },
                                "size_vendor_name": {
                                    "type": "string"
                                },
                                "price_replaced": {
                                    "type": "null"
                                },
                                "price_original": {
                                    "type": "integer"
                                },
                                "price_discount": {
                                    "type": "integer"
                                },
                                "visible": {
                                    "type": "integer"
                                },
                                "active_in_content": {
                                    "type": "integer"
                                },
                                "is_buyable": {
                                    "type": "integer"
                                },
                                "is_count_changeable_by_import": {
                                    "type": "integer"
                                },
                                "weight": {
                                    "type": "string"
                                },
                                "merc_collection": {
                                    "type": "string"
                                },
                                "merc_probe": {
                                    "type": "string"
                                },
                                "created_at": {
                                    "type": "string"
                                },
                                "updated_at": {
                                    "type": "string"
                                },
                                "ext_id_or_guid": {
                                    "type": "string"
                                },
                                "model_id": {
                                    "type": "integer"
                                },
                                "size": {
                                    "type": "object",
                                    "properties": {
                                        "id": {
                                            "type": "integer"
                                        },
                                        "title": {
                                            "type": "string"
                                        },
                                        "title_vnd": {
                                            "type": "string"
                                        },
                                        "visible": {
                                            "type": "integer"
                                        },
                                        "is_visible_in_catalog": {
                                            "type": "integer"
                                        }
                                    },
                                    "required": [
                                        "id",
                                        "title",
                                        "title_vnd",
                                        "visible",
                                        "is_visible_in_catalog"
                                    ]
                                },
                                "sizeAttributes": {
                                    "type": "object",
                                    "properties": {
                                        "russian_label": {
                                            "type": "string"
                                        },
                                        "russian_size": {
                                            "type": "string"
                                        },
                                        "vendor_label": {
                                            "type": "string"
                                        },
                                        "vendor_size": {
                                            "type": "string"
                                        }
                                    },
                                    "required": [
                                        "russian_label",
                                        "russian_size",
                                        "vendor_label",
                                        "vendor_size"
                                    ]
                                },
                                "availabilityInStock": {
                                    "type": "boolean"
                                },
                                "prices": {
                                    "type": "object",
                                    "properties": {
                                        "base": {
                                            "type": "object",
                                            "properties": {
                                                "currency": {
                                                    "type": "string"
                                                },
                                                "priceOriginal": {
                                                    "type": "integer"
                                                },
                                                "priceDiscount": {
                                                    "type": "integer"
                                                }
                                            },
                                            "required": [
                                                "currency",
                                                "priceOriginal",
                                                "priceDiscount"
                                            ]
                                        },
                                        "displayed": {
                                            "type": "object",
                                            "properties": {
                                                "currency": {
                                                    "type": "string"
                                                },
                                                "priceOriginal": {
                                                    "type": "integer"
                                                },
                                                "priceDiscount": {
                                                    "type": "integer"
                                                }
                                            },
                                            "required": [
                                                "currency",
                                                "priceOriginal",
                                                "priceDiscount"
                                            ]
                                        }
                                    },
                                    "required": [
                                        "base",
                                        "displayed"
                                    ]
                                },
                                "additional": {
                                    "type": "object",
                                    "properties": {
                                        "tags": {
                                            "type": "array",
                                            "items": {}
                                        }
                                    },
                                    "required": [
                                        "tags"
                                    ]
                                }
                            },
                            "required": [
                                "id",
                                "content_id",
                                "item_id",
                                "ext_id",
                                "ext_guid",
                                "barcode",
                                "barcode_vnd",
                                "season",
                                "size_id",
                                "size_vendor_name",
                                "price_replaced",
                                "price_original",
                                "price_discount",
                                "visible",
                                "active_in_content",
                                "is_buyable",
                                "is_count_changeable_by_import",
                                "weight",
                                "merc_collection",
                                "merc_probe",
                                "created_at",
                                "updated_at",
                                "ext_id_or_guid",
                                "model_id",
                                "size",
                                "sizeAttributes",
                                "availabilityInStock",
                                "prices",
                                "additional"
                            ]
                        },
                        "brand": {
                            "type": "object",
                            "properties": {
                                "id": {
                                    "type": "integer"
                                },
                                "title": {
                                    "type": "string"
                                },
                                "slug": {
                                    "type": "string"
                                },
                                "size_abbr": {
                                    "type": "string"
                                },
                                "is_privileged": {
                                    "type": "integer"
                                },
                                "is_enough_items_to_show": {
                                    "type": "integer"
                                },
                                "show_always": {
                                    "type": "integer"
                                },
                                "logo_url": {
                                    "type": "string"
                                }
                            },
                            "required": [
                                "id",
                                "title",
                                "slug",
                                "size_abbr",
                                "is_privileged",
                                "is_enough_items_to_show",
                                "show_always",
                                "logo_url"
                            ]
                        },
                        "tags": {
                            "type": "array",
                            "items": {}
                        },
                        "category": {
                            "type": "object",
                            "properties": {
                                "id": {
                                    "type": "integer"
                                },
                                "parent_id": {
                                    "type": "integer"
                                },
                                "title": {
                                    "type": "string"
                                },
                                "slug": {
                                    "type": "string"
                                },
                                "description": {
                                    "type": "string"
                                },
                                "size_dimension": {
                                    "type": "integer"
                                },
                                "is_mercury": {
                                    "type": "integer"
                                },
                                "is_mercury_watch": {
                                    "type": "integer"
                                },
                                "quantity_selector_available": {
                                    "type": "integer"
                                },
                                "root_id": {
                                    "type": "integer"
                                },
                                "root_title": {
                                    "type": "string"
                                },
                                "replacement": {
                                    "type": "object",
                                    "properties": {
                                        "id": {
                                            "type": "integer"
                                        },
                                        "title": {
                                            "type": "string"
                                        },
                                        "slug": {
                                            "type": "string"
                                        }
                                    },
                                    "required": [
                                        "id",
                                        "title",
                                        "slug"
                                    ]
                                }
                            },
                            "required": [
                                "id",
                                "parent_id",
                                "title",
                                "slug",
                                "description",
                                "size_dimension",
                                "is_mercury",
                                "is_mercury_watch",
                                "quantity_selector_available",
                                "root_id",
                                "root_title",
                                "replacement"
                            ]
                        },
                        "is_buyable": {
                            "type": "integer"
                        },
                        "in_stock": {
                            "type": "boolean"
                        },
                        "only_one": {
                            "type": "boolean"
                        },
                        "has_other_sizes": {
                            "type": "boolean"
                        },
                        "size_binding": {
                            "type": "object",
                            "properties": {
                                "brand_root_size_abbr": {
                                    "type": "string"
                                }
                            },
                            "required": [
                                "brand_root_size_abbr"
                            ]
                        },
                        "ext_id": {
                            "type": "string"
                        },
                        "color_code": {
                            "type": "string"
                        },
                        "sum": {
                            "type": "integer"
                        },
                        "ajusted_sum": {
                            "type": "integer"
                        },
                        "coupon_sum": {
                            "type": "integer"
                        },
                        "loyalty_sum": {
                            "type": "integer"
                        },
                        "is_active": {
                            "type": "boolean"
                        },
                        "state_message": {
                            "type": "string"
                        },
                        "countInStockLeft": {
                            "type": "integer"
                        },
                        "countInStockComment": {
                            "type": "string"
                        },
                        "features": {
                            "type": "array",
                            "items": {}
                        },
                        "looks": {
                            "type": "array",
                            "items": {}
                        },
                        "type": {
                            "type": "string"
                        },
                        "prices": {
                            "type": "object",
                            "properties": {
                                "base": {
                                    "type": "object",
                                    "properties": {
                                        "currency": {
                                            "type": "string"
                                        },
                                        "amount": {
                                            "type": "integer"
                                        },
                                        "price": {
                                            "type": "integer"
                                        },
                                        "adjustedAmount": {
                                            "type": "integer"
                                        },
                                        "couponDiscount": {
                                            "type": "integer"
                                        },
                                        "loyaltyAmount": {
                                            "type": "integer"
                                        }
                                    },
                                    "required": [
                                        "currency",
                                        "amount",
                                        "price",
                                        "adjustedAmount",
                                        "couponDiscount",
                                        "loyaltyAmount"
                                    ]
                                },
                                "displayed": {
                                    "type": "object",
                                    "properties": {
                                        "currency": {
                                            "type": "string"
                                        },
                                        "amount": {
                                            "type": "integer"
                                        },
                                        "price": {
                                            "type": "integer"
                                        },
                                        "adjustedAmount": {
                                            "type": "integer"
                                        },
                                        "couponDiscount": {
                                            "type": "integer"
                                        },
                                        "loyaltyAmount": {
                                            "type": "integer"
                                        }
                                    },
                                    "required": [
                                        "currency",
                                        "amount",
                                        "price",
                                        "adjustedAmount",
                                        "couponDiscount",
                                        "loyaltyAmount"
                                    ]
                                }
                            },
                            "required": [
                                "base",
                                "displayed"
                            ]
                        },
                        "quantity": {
                            "type": "integer"
                        },
                        "quantity_in_stock": {
                            "type": "boolean"
                        },
                        "more_in_stock": {
                            "type": "boolean"
                        },
                        "in_wishlist": {
                            "type": "boolean"
                        },
                        "soonStatus": {
                            "type": "boolean"
                        },
                        "availableFrom": {
                            "type": "null"
                        },
                        "coupon_applied": {
                            "type": "boolean"
                        },
                        "selected": {
                            "type": "boolean"
                        },
                        "state": {
                            "type": "integer"
                        }
                    },
                    "required": [
                        "position_id",
                        "item_type",
                        "item_id",
                        "price",
                        "color",
                        "photos",
                        "title",
                        "slug",
                        "description_lit",
                        "sku",
                        "brand",
                        "tags",
                        "category",
                        "is_buyable",
                        "in_stock",
                        "only_one",
                        "has_other_sizes",
                        "size_binding",
                        "ext_id",
                        "color_code",
                        "sum",
                        "ajusted_sum",
                        "coupon_sum",
                        "loyalty_sum",
                        "is_active",
                        "state_message",
                        "countInStockLeft",
                        "countInStockComment",
                        "features",
                        "looks",
                        "type",
                        "prices",
                        "quantity",
                        "quantity_in_stock",
                        "more_in_stock",
                        "in_wishlist",
                        "soonStatus",
                        "availableFrom",
                        "coupon_applied",
                        "selected",
                        "state"
                    ]
                }
            ]
        },
        "notices": {
            "type": "array",
            "items": {}
        },
        "regulations": {
            "type": "array",
            "items": {}
        },
        "bonus_applied": {
            "type": "boolean"
        },
        "bonus": {
            "type": "integer"
        },
        "coupon_code": {
            "type": "null"
        },
        "total_items": {
            "type": "object",
            "properties": {
                "total": {
                    "type": "integer"
                },
                "total_in_stock": {
                    "type": "integer"
                }
            },
            "required": [
                "total",
                "total_in_stock"
            ]
        },
        "total_sum": {
            "type": "integer"
        },
        "total_adjusted_sum": {
            "type": "integer"
        },
        "total_sum_in_stock": {
            "type": "integer"
        },
        "full_amount": {
            "type": "integer"
        },
        "base_discount": {
            "type": "integer"
        },
        "coupon_discount": {
            "type": "integer"
        },
        "prices": {
            "type": "object",
            "properties": {
                "base": {
                    "type": "object",
                    "properties": {
                        "currency": {
                            "type": "string"
                        },
                        "amount": {
                            "type": "integer"
                        },
                        "adjustedAmount": {
                            "type": "integer"
                        },
                        "inStockAmount": {
                            "type": "integer"
                        },
                        "fullAmount": {
                            "type": "integer"
                        },
                        "baseDiscount": {
                            "type": "integer"
                        },
                        "couponDiscount": {
                            "type": "integer"
                        },
                        "catalogDiscount": {
                            "type": "integer"
                        },
                        "ruleDiscount": {
                            "type": "integer"
                        }
                    },
                    "required": [
                        "currency",
                        "amount",
                        "adjustedAmount",
                        "inStockAmount",
                        "fullAmount",
                        "baseDiscount",
                        "couponDiscount",
                        "catalogDiscount",
                        "ruleDiscount"
                    ]
                },
                "displayed": {
                    "type": "object",
                    "properties": {
                        "currency": {
                            "type": "string"
                        },
                        "amount": {
                            "type": "integer"
                        },
                        "adjustedAmount": {
                            "type": "integer"
                        },
                        "inStockAmount": {
                            "type": "integer"
                        },
                        "fullAmount": {
                            "type": "integer"
                        },
                        "baseDiscount": {
                            "type": "integer"
                        },
                        "couponDiscount": {
                            "type": "integer"
                        },
                        "catalogDiscount": {
                            "type": "integer"
                        },
                        "ruleDiscount": {
                            "type": "integer"
                        }
                    },
                    "required": [
                        "currency",
                        "amount",
                        "adjustedAmount",
                        "inStockAmount",
                        "fullAmount",
                        "baseDiscount",
                        "couponDiscount",
                        "catalogDiscount",
                        "ruleDiscount"
                    ]
                }
            },
            "required": [
                "base",
                "displayed"
            ]
        },
        "merged": {
            "type": "boolean"
        },
        "features": {
            "type": "array",
            "items": {}
        },
        "sid": {
            "type": "string"
        }
    },
    "required": [
        "items",
        "notices",
        "regulations",
        "bonus_applied",
        "bonus",
        "coupon_code",
        "total_items",
        "total_sum",
        "total_adjusted_sum",
        "total_sum_in_stock",
        "full_amount",
        "base_discount",
        "coupon_discount",
        "prices",
        "merged",
        "features",
        "sid"
    ]
}
