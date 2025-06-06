from collections import namedtuple

IRecvDevice = namedtuple('IRecvDevice', 'product_type hardware_model board_id chip_id display_name')

IRECV_DEVICES = (
    # iPhone
    IRecvDevice(product_type='iPhone1,1', hardware_model='m68ap', board_id=0x00, chip_id=0x8900,
                display_name='iPhone 2G'),
    IRecvDevice(product_type='iPhone1,2', hardware_model='n82ap', board_id=0x04, chip_id=0x8900,
                display_name='iPhone 3G'),
    IRecvDevice(product_type='iPhone2,1', hardware_model='n88ap', board_id=0x00, chip_id=0x8920,
                display_name='iPhone 3Gs'),
    IRecvDevice(product_type='iPhone3,1', hardware_model='n90ap', board_id=0x00, chip_id=0x8930,
                display_name='iPhone 4 (GSM)'),
    IRecvDevice(product_type='iPhone3,2', hardware_model='n90bap', board_id=0x04, chip_id=0x8930,
                display_name='iPhone 4 (GSM) R2 2012'),
    IRecvDevice(product_type='iPhone3,3', hardware_model='n92ap', board_id=0x06, chip_id=0x8930,
                display_name='iPhone 4 (CDMA)'),
    IRecvDevice(product_type='iPhone4,1', hardware_model='n94ap', board_id=0x08, chip_id=0x8940,
                display_name='iPhone 4s'),
    IRecvDevice(product_type='iPhone5,1', hardware_model='n41ap', board_id=0x00, chip_id=0x8950,
                display_name='iPhone 5 (GSM)'),
    IRecvDevice(product_type='iPhone5,2', hardware_model='n42ap', board_id=0x02, chip_id=0x8950,
                display_name='iPhone 5 (Global)'),
    IRecvDevice(product_type='iPhone5,3', hardware_model='n48ap', board_id=0x0a, chip_id=0x8950,
                display_name='iPhone 5c (GSM)'),
    IRecvDevice(product_type='iPhone5,4', hardware_model='n49ap', board_id=0x0e, chip_id=0x8950,
                display_name='iPhone 5c (Global)'),
    IRecvDevice(product_type='iPhone6,1', hardware_model='n51ap', board_id=0x00, chip_id=0x8960,
                display_name='iPhone 5s (GSM)'),
    IRecvDevice(product_type='iPhone6,2', hardware_model='n53ap', board_id=0x02, chip_id=0x8960,
                display_name='iPhone 5s (Global)'),
    IRecvDevice(product_type='iPhone7,1', hardware_model='n56ap', board_id=0x04, chip_id=0x7000,
                display_name='iPhone 6 Plus'),
    IRecvDevice(product_type='iPhone7,2', hardware_model='n61ap', board_id=0x06, chip_id=0x7000,
                display_name='iPhone 6'),
    IRecvDevice(product_type='iPhone8,1', hardware_model='n71ap', board_id=0x04, chip_id=0x8000,
                display_name='iPhone 6s'),
    IRecvDevice(product_type='iPhone8,1', hardware_model='n71map', board_id=0x04, chip_id=0x8003,
                display_name='iPhone 6s'),
    IRecvDevice(product_type='iPhone8,2', hardware_model='n66ap', board_id=0x06, chip_id=0x8000,
                display_name='iPhone 6s Plus'),
    IRecvDevice(product_type='iPhone8,2', hardware_model='n66map', board_id=0x06, chip_id=0x8003,
                display_name='iPhone 6s Plus'),
    IRecvDevice(product_type='iPhone8,4', hardware_model='n69ap', board_id=0x02, chip_id=0x8003,
                display_name='iPhone SE (1st gen)'),
    IRecvDevice(product_type='iPhone8,4', hardware_model='n69uap', board_id=0x02, chip_id=0x8000,
                display_name='iPhone SE (1st gen)'),
    IRecvDevice(product_type='iPhone9,1', hardware_model='d10ap', board_id=0x08, chip_id=0x8010,
                display_name='iPhone 7 (Global)'),
    IRecvDevice(product_type='iPhone9,2', hardware_model='d11ap', board_id=0x0a, chip_id=0x8010,
                display_name='iPhone 7 Plus (Global)'),
    IRecvDevice(product_type='iPhone9,3', hardware_model='d101ap', board_id=0x0c, chip_id=0x8010,
                display_name='iPhone 7 (GSM)'),
    IRecvDevice(product_type='iPhone9,4', hardware_model='d111ap', board_id=0x0e, chip_id=0x8010,
                display_name='iPhone 7 Plus (GSM)'),
    IRecvDevice(product_type='iPhone10,1', hardware_model='d20ap', board_id=0x02, chip_id=0x8015,
                display_name='iPhone 8 (Global)'),
    IRecvDevice(product_type='iPhone10,2', hardware_model='d21ap', board_id=0x04, chip_id=0x8015,
                display_name='iPhone 8 Plus (Global)'),
    IRecvDevice(product_type='iPhone10,3', hardware_model='d22ap', board_id=0x06, chip_id=0x8015,
                display_name='iPhone X (Global)'),
    IRecvDevice(product_type='iPhone10,4', hardware_model='d201ap', board_id=0x0a, chip_id=0x8015,
                display_name='iPhone 8 (GSM)'),
    IRecvDevice(product_type='iPhone10,5', hardware_model='d211ap', board_id=0x0c, chip_id=0x8015,
                display_name='iPhone 8 Plus (GSM)'),
    IRecvDevice(product_type='iPhone10,6', hardware_model='d221ap', board_id=0x0e, chip_id=0x8015,
                display_name='iPhone X (GSM)'),
    IRecvDevice(product_type='iPhone11,2', hardware_model='d321ap', board_id=0x0e, chip_id=0x8020,
                display_name='iPhone XS'),
    IRecvDevice(product_type='iPhone11,4', hardware_model='d331ap', board_id=0x0a, chip_id=0x8020,
                display_name='iPhone XS Max (China)'),
    IRecvDevice(product_type='iPhone11,6', hardware_model='d331pap', board_id=0x1a, chip_id=0x8020,
                display_name='iPhone XS Max'),
    IRecvDevice(product_type='iPhone11,8', hardware_model='n841ap', board_id=0x0c, chip_id=0x8020,
                display_name='iPhone XR'),
    IRecvDevice(product_type='iPhone12,1', hardware_model='n104ap', board_id=0x04, chip_id=0x8030,
                display_name='iPhone 11'),
    IRecvDevice(product_type='iPhone12,3', hardware_model='d421ap', board_id=0x06, chip_id=0x8030,
                display_name='iPhone 11 Pro'),
    IRecvDevice(product_type='iPhone12,5', hardware_model='d431ap', board_id=0x02, chip_id=0x8030,
                display_name='iPhone 11 Pro Max'),
    IRecvDevice(product_type='iPhone12,8', hardware_model='d79ap', board_id=0x10, chip_id=0x8030,
                display_name='iPhone SE (2nd gen)'),
    IRecvDevice(product_type='iPhone13,1', hardware_model='d52gap', board_id=0x0A, chip_id=0x8101,
                display_name='iPhone 12 mini'),
    IRecvDevice(product_type='iPhone13,2', hardware_model='d53gap', board_id=0x0C, chip_id=0x8101,
                display_name='iPhone 12'),
    IRecvDevice(product_type='iPhone13,3', hardware_model='d53pap', board_id=0x0E, chip_id=0x8101,
                display_name='iPhone 12 Pro'),
    IRecvDevice(product_type='iPhone13,4', hardware_model='d54pap', board_id=0x08, chip_id=0x8101,
                display_name='iPhone 12 Pro Max'),
    IRecvDevice(product_type='iPhone14,2', hardware_model='d63ap', board_id=0x0C, chip_id=0x8110,
                display_name='iPhone 13 Pro'),
    IRecvDevice(product_type='iPhone14,3', hardware_model='d64ap', board_id=0x0E, chip_id=0x8110,
                display_name='iPhone 13 Pro Max'),
    IRecvDevice(product_type='iPhone14,4', hardware_model='d16ap', board_id=0x08, chip_id=0x8110,
                display_name='iPhone 13 mini'),
    IRecvDevice(product_type='iPhone14,5', hardware_model='d17ap', board_id=0x0A, chip_id=0x8110,
                display_name='iPhone 13'),
    IRecvDevice(product_type='iPhone14,6', hardware_model='d49ap', board_id=0x10, chip_id=0x8110,
                display_name='iPhone SE (3rd gen)'),
    IRecvDevice(product_type='iPhone14,7', hardware_model='d27ap', board_id=0x18, chip_id=0x8110,
                display_name='iPhone 14'),
    IRecvDevice(product_type='iPhone14,8', hardware_model='d28ap', board_id=0x1A, chip_id=0x8110,
                display_name='iPhone 14 Plus'),
    IRecvDevice(product_type='iPhone15,2', hardware_model='d73ap', board_id=0x0C, chip_id=0x8120,
                display_name='iPhone 14 Pro'),
    IRecvDevice(product_type='iPhone15,3', hardware_model='d74ap', board_id=0x0E, chip_id=0x8120,
                display_name='iPhone 14 Pro Max'),
    IRecvDevice(product_type='iPhone15,4', hardware_model='d37ap', board_id=0x08, chip_id=0x8120,
                display_name='iPhone 15'),
    IRecvDevice(product_type='iPhone15,5', hardware_model='d38ap', board_id=0x0A, chip_id=0x8120,
                display_name='iPhone 15 Plus'),
    IRecvDevice(product_type='iPhone16,1', hardware_model='d83ap', board_id=0x04, chip_id=0x8130,
                display_name='iPhone 15 Pro'),
    IRecvDevice(product_type='iPhone16,2', hardware_model='d84ap', board_id=0x06, chip_id=0x8130,
                display_name='iPhone 15 Pro Max'),
    IRecvDevice(product_type='iPhone17,3', hardware_model='d47ap', board_id=0x08, chip_id=0x8140,
                display_name='iPhone 16'),
    IRecvDevice(product_type='iPhone17,4', hardware_model='d48ap', board_id=0x0A, chip_id=0x8140,
                display_name='iPhone 16 Plus'),
    IRecvDevice(product_type='iPhone17,5', hardware_model='v59ap', board_id=0x04, chip_id=0x8140,
                display_name='iPhone 16e'),
    IRecvDevice(product_type='iPhone17,1', hardware_model='d93ap', board_id=0x0C, chip_id=0x8140,
                display_name='iPhone 16 Pro'),
    IRecvDevice(product_type='iPhone17,2', hardware_model='d94ap', board_id=0x0E, chip_id=0x8140,
                display_name='iPhone 16 Pro Max'),
    # iPod
    IRecvDevice(product_type='iPod1,1', hardware_model='n45ap', board_id=0x02, chip_id=0x8900,
                display_name='iPod Touch (1st gen)'),
    IRecvDevice(product_type='iPod2,1', hardware_model='n72ap', board_id=0x00, chip_id=0x8720,
                display_name='iPod Touch (2nd gen)'),
    IRecvDevice(product_type='iPod3,1', hardware_model='n18ap', board_id=0x02, chip_id=0x8922,
                display_name='iPod Touch (3rd gen)'),
    IRecvDevice(product_type='iPod4,1', hardware_model='n81ap', board_id=0x08, chip_id=0x8930,
                display_name='iPod Touch (4th gen)'),
    IRecvDevice(product_type='iPod5,1', hardware_model='n78ap', board_id=0x00, chip_id=0x8942,
                display_name='iPod Touch (5th gen)'),
    IRecvDevice(product_type='iPod7,1', hardware_model='n102ap', board_id=0x10, chip_id=0x7000,
                display_name='iPod Touch (6th gen)'),
    IRecvDevice(product_type='iPod9,1', hardware_model='n112ap', board_id=0x16, chip_id=0x8010,
                display_name='iPod Touch (7th gen)'),
    # iPad
    IRecvDevice(product_type='iPad1,1', hardware_model='k48ap', board_id=0x02, chip_id=0x8930, display_name='iPad'),
    IRecvDevice(product_type='iPad2,1', hardware_model='k93ap', board_id=0x04, chip_id=0x8940,
                display_name='iPad 2 (WiFi)'),
    IRecvDevice(product_type='iPad2,2', hardware_model='k94ap', board_id=0x06, chip_id=0x8940,
                display_name='iPad 2 (GSM)'),
    IRecvDevice(product_type='iPad2,3', hardware_model='k95ap', board_id=0x02, chip_id=0x8940,
                display_name='iPad 2 (CDMA)'),
    IRecvDevice(product_type='iPad2,4', hardware_model='k93aap', board_id=0x06, chip_id=0x8942,
                display_name='iPad 2 (WiFi) R2 2012'),
    IRecvDevice(product_type='iPad2,5', hardware_model='p105ap', board_id=0x0a, chip_id=0x8942,
                display_name='iPad mini (WiFi)'),
    IRecvDevice(product_type='iPad2,6', hardware_model='p106ap', board_id=0x0c, chip_id=0x8942,
                display_name='iPad mini (GSM)'),
    IRecvDevice(product_type='iPad2,7', hardware_model='p107ap', board_id=0x0e, chip_id=0x8942,
                display_name='iPad mini (Global)'),
    IRecvDevice(product_type='iPad3,1', hardware_model='j1ap', board_id=0x00, chip_id=0x8945,
                display_name='iPad (3rd gen, WiFi)'),
    IRecvDevice(product_type='iPad3,2', hardware_model='j2ap', board_id=0x02, chip_id=0x8945,
                display_name='iPad (3rd gen, CDMA)'),
    IRecvDevice(product_type='iPad3,3', hardware_model='j2aap', board_id=0x04, chip_id=0x8945,
                display_name='iPad (3rd gen, GSM)'),
    IRecvDevice(product_type='iPad3,4', hardware_model='p101ap', board_id=0x00, chip_id=0x8955,
                display_name='iPad (4th gen, WiFi)'),
    IRecvDevice(product_type='iPad3,5', hardware_model='p102ap', board_id=0x02, chip_id=0x8955,
                display_name='iPad (4th gen, GSM)'),
    IRecvDevice(product_type='iPad3,6', hardware_model='p103ap', board_id=0x04, chip_id=0x8955,
                display_name='iPad (4th gen, Global)'),
    IRecvDevice(product_type='iPad4,1', hardware_model='j71ap', board_id=0x10, chip_id=0x8960,
                display_name='iPad Air (WiFi)'),
    IRecvDevice(product_type='iPad4,2', hardware_model='j72ap', board_id=0x12, chip_id=0x8960,
                display_name='iPad Air (Cellular)'),
    IRecvDevice(product_type='iPad4,3', hardware_model='j73ap', board_id=0x14, chip_id=0x8960,
                display_name='iPad Air (China)'),
    IRecvDevice(product_type='iPad4,4', hardware_model='j85ap', board_id=0x0a, chip_id=0x8960,
                display_name='iPad mini 2 (WiFi)'),
    IRecvDevice(product_type='iPad4,5', hardware_model='j86ap', board_id=0x0c, chip_id=0x8960,
                display_name='iPad mini 2 (Cellular)'),
    IRecvDevice(product_type='iPad4,6', hardware_model='j87ap', board_id=0x0e, chip_id=0x8960,
                display_name='iPad mini 2 (China)'),
    IRecvDevice(product_type='iPad4,7', hardware_model='j85map', board_id=0x32, chip_id=0x8960,
                display_name='iPad mini 3 (WiFi)'),
    IRecvDevice(product_type='iPad4,8', hardware_model='j86map', board_id=0x34, chip_id=0x8960,
                display_name='iPad mini 3 (Cellular)'),
    IRecvDevice(product_type='iPad4,9', hardware_model='j87map', board_id=0x36, chip_id=0x8960,
                display_name='iPad mini 3 (China)'),
    IRecvDevice(product_type='iPad5,1', hardware_model='j96ap', board_id=0x08, chip_id=0x7000,
                display_name='iPad mini 4 (WiFi)'),
    IRecvDevice(product_type='iPad5,2', hardware_model='j97ap', board_id=0x0A, chip_id=0x7000,
                display_name='iPad mini 4 (Cellular)'),
    IRecvDevice(product_type='iPad5,3', hardware_model='j81ap', board_id=0x06, chip_id=0x7001,
                display_name='iPad Air 2 (WiFi)'),
    IRecvDevice(product_type='iPad5,4', hardware_model='j82ap', board_id=0x02, chip_id=0x7001,
                display_name='iPad Air 2 (Cellular)'),
    IRecvDevice(product_type='iPad6,3', hardware_model='j127ap', board_id=0x08, chip_id=0x8001,
                display_name='iPad Pro 9.7-inch (WiFi)'),
    IRecvDevice(product_type='iPad6,4', hardware_model='j128ap', board_id=0x0a, chip_id=0x8001,
                display_name='iPad Pro 9.7-inch (Cellular)'),
    IRecvDevice(product_type='iPad6,7', hardware_model='j98aap', board_id=0x10, chip_id=0x8001,
                display_name='iPad Pro 12.9-inch (1st gen, WiFi)'),
    IRecvDevice(product_type='iPad6,8', hardware_model='j99aap', board_id=0x12, chip_id=0x8001,
                display_name='iPad Pro 12.9-inch (1st gen, Cellular)'),
    IRecvDevice(product_type='iPad6,11', hardware_model='j71sap', board_id=0x10, chip_id=0x8000,
                display_name='iPad (5th gen, WiFi)'),
    IRecvDevice(product_type='iPad6,11', hardware_model='j71tap', board_id=0x10, chip_id=0x8003,
                display_name='iPad (5th gen, WiFi)'),
    IRecvDevice(product_type='iPad6,12', hardware_model='j72sap', board_id=0x12, chip_id=0x8000,
                display_name='iPad (5th gen, Cellular)'),
    IRecvDevice(product_type='iPad6,12', hardware_model='j72tap', board_id=0x12, chip_id=0x8003,
                display_name='iPad (5th gen, Cellular)'),
    IRecvDevice(product_type='iPad7,1', hardware_model='j120ap', board_id=0x0C, chip_id=0x8011,
                display_name='iPad Pro 12.9-inch (2nd gen, WiFi)'),
    IRecvDevice(product_type='iPad7,2', hardware_model='j121ap', board_id=0x0E, chip_id=0x8011,
                display_name='iPad Pro 12.9-inch (2nd gen, Cellular)'),
    IRecvDevice(product_type='iPad7,3', hardware_model='j207ap', board_id=0x04, chip_id=0x8011,
                display_name='iPad Pro 10.5-inch (WiFi)'),
    IRecvDevice(product_type='iPad7,4', hardware_model='j208ap', board_id=0x06, chip_id=0x8011,
                display_name='iPad Pro 10.5-inch (Cellular)'),
    IRecvDevice(product_type='iPad7,5', hardware_model='j71bap', board_id=0x18, chip_id=0x8010,
                display_name='iPad (6th gen, WiFi)'),
    IRecvDevice(product_type='iPad7,6', hardware_model='j72bap', board_id=0x1A, chip_id=0x8010,
                display_name='iPad (6th gen, Cellular)'),
    IRecvDevice(product_type='iPad7,11', hardware_model='j171ap', board_id=0x1C, chip_id=0x8010,
                display_name='iPad (7th gen, WiFi)'),
    IRecvDevice(product_type='iPad7,12', hardware_model='j172ap', board_id=0x1E, chip_id=0x8010,
                display_name='iPad (7th gen, Cellular)'),
    IRecvDevice(product_type='iPad8,1', hardware_model='j317ap', board_id=0x0C, chip_id=0x8027,
                display_name='iPad Pro 11-inch (1st gen, WiFi)'),
    IRecvDevice(product_type='iPad8,2', hardware_model='j317xap', board_id=0x1C, chip_id=0x8027,
                display_name='iPad Pro 11-inch (1st gen, WiFi, 1TB)'),
    IRecvDevice(product_type='iPad8,3', hardware_model='j318ap', board_id=0x0E, chip_id=0x8027,
                display_name='iPad Pro 11-inch (1st gen, Cellular)'),
    IRecvDevice(product_type='iPad8,4', hardware_model='j318xap', board_id=0x1E, chip_id=0x8027,
                display_name='iPad Pro 11-inch (1st gen, Cellular, 1TB)'),
    IRecvDevice(product_type='iPad8,5', hardware_model='j320ap', board_id=0x08, chip_id=0x8027,
                display_name='iPad Pro 12.9-inch (3rd gen, WiFi)'),
    IRecvDevice(product_type='iPad8,6', hardware_model='j320xap', board_id=0x18, chip_id=0x8027,
                display_name='iPad Pro 12.9-inch (3rd gen, WiFi, 1TB)'),
    IRecvDevice(product_type='iPad8,7', hardware_model='j321ap', board_id=0x0A, chip_id=0x8027,
                display_name='iPad Pro 12.9-inch (3rd gen, Cellular)'),
    IRecvDevice(product_type='iPad8,8', hardware_model='j321xap', board_id=0x1A, chip_id=0x8027,
                display_name='iPad Pro 12.9-inch (3rd gen, Cellular, 1TB)'),
    IRecvDevice(product_type='iPad8,9', hardware_model='j417ap', board_id=0x3C, chip_id=0x8027,
                display_name='iPad Pro 11-inch (2nd gen, WiFi)'),
    IRecvDevice(product_type='iPad8,10', hardware_model='j418ap', board_id=0x3E, chip_id=0x8027,
                display_name='iPad Pro 11-inch (2nd gen, Cellular)'),
    IRecvDevice(product_type='iPad8,11', hardware_model='j420ap', board_id=0x38, chip_id=0x8027,
                display_name='iPad Pro 12.9-inch (4th gen, WiFi)'),
    IRecvDevice(product_type='iPad8,12', hardware_model='j421ap', board_id=0x3A, chip_id=0x8027,
                display_name='iPad Pro 12.9-inch (4th gen, Cellular)'),
    IRecvDevice(product_type='iPad11,1', hardware_model='j210ap', board_id=0x14, chip_id=0x8020,
                display_name='iPad mini (5th gen, WiFi)'),
    IRecvDevice(product_type='iPad11,2', hardware_model='j211ap', board_id=0x16, chip_id=0x8020,
                display_name='iPad mini (5th gen, Cellular)'),
    IRecvDevice(product_type='iPad11,3', hardware_model='j217ap', board_id=0x1C, chip_id=0x8020,
                display_name='iPad Air (3rd gen, WiFi)'),
    IRecvDevice(product_type='iPad11,4', hardware_model='j218ap', board_id=0x1E, chip_id=0x8020,
                display_name='iPad Air (3rd gen, Celluar)'),
    IRecvDevice(product_type='iPad11,6', hardware_model='j171aap', board_id=0x24, chip_id=0x8020,
                display_name='iPad (8th gen, WiFi)'),
    IRecvDevice(product_type='iPad11,7', hardware_model='j172aap', board_id=0x26, chip_id=0x8020,
                display_name='iPad (8th gen, Cellular)'),
    IRecvDevice(product_type='iPad12,1', hardware_model='j181ap', board_id=0x18, chip_id=0x8030,
                display_name='iPad (9th gen, WiFi)'),
    IRecvDevice(product_type='iPad12,2', hardware_model='j182ap', board_id=0x1A, chip_id=0x8030,
                display_name='iPad (9th gen, Cellular)'),
    IRecvDevice(product_type='iPad13,1', hardware_model='j307ap', board_id=0x04, chip_id=0x8101,
                display_name='iPad Air (4th gen, WiFi)'),
    IRecvDevice(product_type='iPad13,2', hardware_model='j308ap', board_id=0x06, chip_id=0x8101,
                display_name='iPad Air (4th gen, Celluar)'),
    IRecvDevice(product_type='iPad13,4', hardware_model='j517ap', board_id=0x08, chip_id=0x8103,
                display_name='iPad Pro 11-inch (3rd gen, WiFi)'),
    IRecvDevice(product_type='iPad13,5', hardware_model='j517xap', board_id=0x0A, chip_id=0x8103,
                display_name='iPad Pro 11-inch (3rd gen, WiFi, 2TB)'),
    IRecvDevice(product_type='iPad13,6', hardware_model='j518ap', board_id=0x0C, chip_id=0x8103,
                display_name='iPad Pro 11-inch (3rd gen, Cellular)'),
    IRecvDevice(product_type='iPad13,7', hardware_model='j518xap', board_id=0x0E, chip_id=0x8103,
                display_name='iPad Pro 11-inch (3rd gen, Cellular, 2TB)'),
    IRecvDevice(product_type='iPad13,8', hardware_model='j522ap', board_id=0x18, chip_id=0x8103,
                display_name='iPad Pro 12.9-inch (5th gen, WiFi)'),
    IRecvDevice(product_type='iPad13,9', hardware_model='j522xap', board_id=0x1A, chip_id=0x8103,
                display_name='iPad Pro 12.9-inch (5th gen, WiFi, 2TB)'),
    IRecvDevice(product_type='iPad13,10', hardware_model='j523ap', board_id=0x1C, chip_id=0x8103,
                display_name='iPad Pro 12.9-inch (5th gen, Cellular)'),
    IRecvDevice(product_type='iPad13,11', hardware_model='j523xap', board_id=0x1E, chip_id=0x8103,
                display_name='iPad Pro 12.9-inch (5th gen, Cellular, 2TB)'),
    IRecvDevice(product_type='iPad13,16', hardware_model='j407ap', board_id=0x10, chip_id=0x8103,
                display_name='iPad Air (5th gen, WiFi)'),
    IRecvDevice(product_type='iPad13,17', hardware_model='j408ap', board_id=0x12, chip_id=0x8103,
                display_name='iPad Air (5th gen, Celluar)'),
    IRecvDevice(product_type='iPad14,1', hardware_model='j310ap', board_id=0x04, chip_id=0x8110,
                display_name='iPad mini (6th gen, WiFi)'),
    IRecvDevice(product_type='iPad14,2', hardware_model='j311ap', board_id=0x06, chip_id=0x8110,
                display_name='iPad mini (6th gen, Cellular)'),
    # Apple TV
    IRecvDevice(product_type='AppleTV2,1', hardware_model='k66ap', board_id=0x10, chip_id=0x8930,
                display_name='Apple TV 2'),
    IRecvDevice(product_type='AppleTV3,1', hardware_model='j33ap', board_id=0x08, chip_id=0x8942,
                display_name='Apple TV 3'),
    IRecvDevice(product_type='AppleTV3,2', hardware_model='j33iap', board_id=0x00, chip_id=0x8947,
                display_name='Apple TV 3 (2013)'),
    IRecvDevice(product_type='AppleTV5,3', hardware_model='j42dap', board_id=0x34, chip_id=0x7000,
                display_name='Apple TV 4'),
    IRecvDevice(product_type='AppleTV6,2', hardware_model='j105aap', board_id=0x02, chip_id=0x8011,
                display_name='Apple TV 4K'),
    IRecvDevice(product_type='AppleTV11,1', hardware_model='j305ap', board_id=0x08, chip_id=0x8020,
                display_name='Apple TV 4K (2nd gen)'),
    # HomePod
    IRecvDevice(product_type='AudioAccessory1,1', hardware_model='b238aap', board_id=0x38, chip_id=0x7000,
                display_name='HomePod'),
    IRecvDevice(product_type='AudioAccessory1,2', hardware_model='b238ap', board_id=0x1A, chip_id=0x7000,
                display_name='HomePod'),
    IRecvDevice(product_type='AudioAccessory5,1', hardware_model='b520ap', board_id=0x22, chip_id=0x8006,
                display_name='HomePod mini'),
    # Apple Watch
    IRecvDevice(product_type='Watch1,1', hardware_model='n27aap', board_id=0x02, chip_id=0x7002,
                display_name='Apple Watch 38mm (1st gen)'),
    IRecvDevice(product_type='Watch1,2', hardware_model='n28aap', board_id=0x04, chip_id=0x7002,
                display_name='Apple Watch 42mm (1st gen)'),
    IRecvDevice(product_type='Watch2,6', hardware_model='n27dap', board_id=0x02, chip_id=0x8002,
                display_name='Apple Watch Series 1 (38mm)'),
    IRecvDevice(product_type='Watch2,7', hardware_model='n28dap', board_id=0x04, chip_id=0x8002,
                display_name='Apple Watch Series 1 (42mm)'),
    IRecvDevice(product_type='Watch2,3', hardware_model='n74ap', board_id=0x0C, chip_id=0x8002,
                display_name='Apple Watch Series 2 (38mm)'),
    IRecvDevice(product_type='Watch2,4', hardware_model='n75ap', board_id=0x0E, chip_id=0x8002,
                display_name='Apple Watch Series 2 (42mm)'),
    IRecvDevice(product_type='Watch3,1', hardware_model='n111sap', board_id=0x1C, chip_id=0x8004,
                display_name='Apple Watch Series 3 (38mm Cellular)'),
    IRecvDevice(product_type='Watch3,2', hardware_model='n111bap', board_id=0x1E, chip_id=0x8004,
                display_name='Apple Watch Series 3 (42mm Cellular)'),
    IRecvDevice(product_type='Watch3,3', hardware_model='n121sap', board_id=0x18, chip_id=0x8004,
                display_name='Apple Watch Series 3 (38mm)'),
    IRecvDevice(product_type='Watch3,4', hardware_model='n121bap', board_id=0x1A, chip_id=0x8004,
                display_name='Apple Watch Series 3 (42mm)'),
    IRecvDevice(product_type='Watch4,1', hardware_model='n131sap', board_id=0x08, chip_id=0x8006,
                display_name='Apple Watch Series 4 (40mm)'),
    IRecvDevice(product_type='Watch4,2', hardware_model='n131bap', board_id=0x0A, chip_id=0x8006,
                display_name='Apple Watch Series 4 (44mm)'),
    IRecvDevice(product_type='Watch4,3', hardware_model='n141sap', board_id=0x0C, chip_id=0x8006,
                display_name='Apple Watch Series 4 (40mm Cellular)'),
    IRecvDevice(product_type='Watch4,4', hardware_model='n141bap', board_id=0x0E, chip_id=0x8006,
                display_name='Apple Watch Series 4 (44mm Cellular)'),
    IRecvDevice(product_type='Watch5,1', hardware_model='n144sap', board_id=0x10, chip_id=0x8006,
                display_name='Apple Watch Series 5 (40mm)'),
    IRecvDevice(product_type='Watch5,2', hardware_model='n144bap', board_id=0x12, chip_id=0x8006,
                display_name='Apple Watch Series 5 (44mm)'),
    IRecvDevice(product_type='Watch5,3', hardware_model='n146sap', board_id=0x14, chip_id=0x8006,
                display_name='Apple Watch Series 5 (40mm Cellular)'),
    IRecvDevice(product_type='Watch5,4', hardware_model='n146bap', board_id=0x16, chip_id=0x8006,
                display_name='Apple Watch Series 5 (44mm Cellular)'),
    IRecvDevice(product_type='Watch5,9', hardware_model='n140sap', board_id=0x28, chip_id=0x8006,
                display_name='Apple Watch SE (40mm)'),
    IRecvDevice(product_type='Watch5,10', hardware_model='n140bap', board_id=0x2A, chip_id=0x8006,
                display_name='Apple Watch SE (44mm)'),
    IRecvDevice(product_type='Watch5,11', hardware_model='n142sap', board_id=0x2C, chip_id=0x8006,
                display_name='Apple Watch SE (40mm Cellular)'),
    IRecvDevice(product_type='Watch5,12', hardware_model='n142bap', board_id=0x2E, chip_id=0x8006,
                display_name='Apple Watch SE (44mm Cellular)'),
    IRecvDevice(product_type='Watch6,1', hardware_model='n157sap', board_id=0x08, chip_id=0x8301,
                display_name='Apple Watch Series 6 (40mm)'),
    IRecvDevice(product_type='Watch6,2', hardware_model='n157bap', board_id=0x0A, chip_id=0x8301,
                display_name='Apple Watch Series 6 (44mm)'),
    IRecvDevice(product_type='Watch6,3', hardware_model='n158sap', board_id=0x0C, chip_id=0x8301,
                display_name='Apple Watch Series 6 (40mm Cellular)'),
    IRecvDevice(product_type='Watch6,4', hardware_model='n158bap', board_id=0x0E, chip_id=0x8301,
                display_name='Apple Watch Series 6 (44mm Cellular)'),
    IRecvDevice(product_type='Watch6,6', hardware_model='n187sap', board_id=0x10, chip_id=0x8301,
                display_name='Apple Watch Series 7 (41mm)'),
    IRecvDevice(product_type='Watch6,7', hardware_model='n187bap', board_id=0x12, chip_id=0x8301,
                display_name='Apple Watch Series 7 (45mm)'),
    IRecvDevice(product_type='Watch6,8', hardware_model='n188sap', board_id=0x14, chip_id=0x8301,
                display_name='Apple Watch Series 7 (41mm Cellular)'),
    IRecvDevice(product_type='Watch6,9', hardware_model='n188bap', board_id=0x16, chip_id=0x8301,
                display_name='Apple Watch Series 7 (45mm Cellular)'),
    IRecvDevice(product_type='Watch6,10', hardware_model='n143sap', board_id=0x18, chip_id=0x8301,
                display_name='Apple Watch SE (2nd generation) (40mm)'),
    IRecvDevice(product_type='Watch6,11', hardware_model='n143bap', board_id=0x2A, chip_id=0x8301,
                display_name='Apple Watch SE (2nd generation) (44mm)'),
    IRecvDevice(product_type='Watch6,12', hardware_model='n149sap', board_id=0x2C, chip_id=0x8301,
                display_name='Apple Watch SE (2nd generation) (40mm Cellular)'),
    IRecvDevice(product_type='Watch6,13', hardware_model='n149bap', board_id=0x2E, chip_id=0x8301,
                display_name='Apple Watch SE (2nd generation) (44m Cellular)'),
    IRecvDevice(product_type='Watch6,14', hardware_model='n197sap', board_id=0x30, chip_id=0x8301,
                display_name='Apple Watch Series 8 (41mm)'),
    IRecvDevice(product_type='Watch6,15', hardware_model='n197bap', board_id=0x32, chip_id=0x8301,
                display_name='Apple Watch Series 8 (45mm)'),
    IRecvDevice(product_type='Watch6,16', hardware_model='n198sap', board_id=0x34, chip_id=0x8301,
                display_name='Apple Watch Series 8 (41mm Cellular)'),
    IRecvDevice(product_type='Watch6,17', hardware_model='n198bap', board_id=0x36, chip_id=0x8301,
                display_name='Apple Watch Series 8 (45mm Cellular)'),
    IRecvDevice(product_type='Watch6,17', hardware_model='n199ap', board_id=0x26, chip_id=0x8301,
                display_name='Apple Watch Ultra'),
    IRecvDevice(product_type='Watch7,1', hardware_model='n207sap', board_id=0x08, chip_id=0x8310,
                display_name='Apple Watch Series 9 (41mm)'),
    IRecvDevice(product_type='Watch7,2', hardware_model='n207bap', board_id=0x0A, chip_id=0x8310,
                display_name='Apple Watch Series 9 (45mm)'),
    IRecvDevice(product_type='Watch7,3', hardware_model='n208sap', board_id=0x0C, chip_id=0x8310,
                display_name='Apple Watch Series 9 (41mm Cellular)'),
    IRecvDevice(product_type='Watch7,4', hardware_model='n208bap', board_id=0x0E, chip_id=0x8310,
                display_name='Apple Watch Series 9 (45mm Cellular)'),
    IRecvDevice(product_type='Watch7,5', hardware_model='n210ap', board_id=0x02, chip_id=0x8310,
                display_name='Apple Watch Ultra 2'),
    IRecvDevice(product_type='Watch7,8', hardware_model='n217sap', board_id=0x10, chip_id=0x8310,
                display_name='Apple Watch Series 10 (42mm)'),
    IRecvDevice(product_type='Watch7,9', hardware_model='n217bap', board_id=0x12, chip_id=0x8310,
                display_name='Apple Watch Series 10 (46mm)'),
    IRecvDevice(product_type='Watch7,10', hardware_model='n218sap', board_id=0x14, chip_id=0x8310,
                display_name='Apple Watch Series 10 (42mm Cellular)'),
    IRecvDevice(product_type='Watch7,11', hardware_model='n218bap', board_id=0x16, chip_id=0x8310,
                display_name='Apple Watch Series 10 (46mm Cellular)'),
    # Apple Silicon Macs
    IRecvDevice(product_type='ADP3,2', hardware_model='j273aap', board_id=0x42, chip_id=0x8027,
                display_name='Developer Transition Kit (2020)'),
    IRecvDevice(product_type='Macmini9,1', hardware_model='j274ap', board_id=0x22, chip_id=0x8103,
                display_name='Mac mini (M1, 2020)'),
    IRecvDevice(product_type='MacBookPro17,1', hardware_model='j293ap', board_id=0x24, chip_id=0x8103,
                display_name='MacBook Pro (M1, 13-inch, 2020)'),
    IRecvDevice(product_type='MacBookPro18,1', hardware_model='j316sap', board_id=0x0A, chip_id=0x6000,
                display_name='MacBook Pro (M1 Pro, 16-inch, 2021)'),
    IRecvDevice(product_type='MacBookPro18,2', hardware_model='j316cap', board_id=0x0A, chip_id=0x6001,
                display_name='MacBook Pro (M1 Max, 16-inch, 2021)'),
    IRecvDevice(product_type='MacBookPro18,3', hardware_model='j314sap', board_id=0x08, chip_id=0x6000,
                display_name='MacBook Pro (M1 Pro, 14-inch, 2021)'),
    IRecvDevice(product_type='MacBookPro18,4', hardware_model='j314cap', board_id=0x08, chip_id=0x6001,
                display_name='MacBook Pro (M1 Max, 14-inch, 2021)'),
    IRecvDevice(product_type='MacBookAir10,1', hardware_model='j313ap', board_id=0x26, chip_id=0x8103,
                display_name='MacBook Air (M1, 2020)'),
    IRecvDevice(product_type='iMac21,1', hardware_model='j456ap', board_id=0x28, chip_id=0x8103,
                display_name='iMac 24-inch (M1, Two Ports, 2021)'),
    IRecvDevice(product_type='iMac21,2', hardware_model='j457ap', board_id=0x2A, chip_id=0x8103,
                display_name='iMac 24-inch (M1, Four Ports, 2021)'),
    IRecvDevice(product_type='Mac13,1', hardware_model='j375cap', board_id=0x04, chip_id=0x6001,
                display_name='Mac Studio (M1 Max, 2022)'),
    IRecvDevice(product_type='Mac13,2', hardware_model='j375dap', board_id=0x0C, chip_id=0x6002,
                display_name='Mac Studio (M1 Ultra, 2022)'),
    IRecvDevice(product_type='Mac14,2', hardware_model='j413ap', board_id=0x28, chip_id=0x8112,
                display_name='MacBook Air (M2, 2022)'),
    IRecvDevice(product_type='Mac14,7', hardware_model='j493ap', board_id=0x2A, chip_id=0x8112,
                display_name='MacBook Pro (M2, 13-inch, 2022)'),
    # Apple T2 Coprocessor
    IRecvDevice(product_type='iBridge2,1', hardware_model='j137ap', board_id=0x0A, chip_id=0x8012,
                display_name='Apple T2 iMacPro1,1 (j137)'),
    IRecvDevice(product_type='iBridge2,3', hardware_model='j680ap', board_id=0x0B, chip_id=0x8012,
                display_name='Apple T2 MacBookPro15,1 (j680)'),
    IRecvDevice(product_type='iBridge2,4', hardware_model='j132ap', board_id=0x0C, chip_id=0x8012,
                display_name='Apple T2 MacBookPro15,2 (j132)'),
    IRecvDevice(product_type='iBridge2,5', hardware_model='j174ap', board_id=0x0E, chip_id=0x8012,
                display_name='Apple T2 Macmini8,1 (j174)'),
    IRecvDevice(product_type='iBridge2,6', hardware_model='j160ap', board_id=0x0F, chip_id=0x8012,
                display_name='Apple T2 MacPro7,1 (j160)'),
    IRecvDevice(product_type='iBridge2,7', hardware_model='j780ap', board_id=0x07, chip_id=0x8012,
                display_name='Apple T2 MacBookPro15,3 (j780)'),
    IRecvDevice(product_type='iBridge2,8', hardware_model='j140kap', board_id=0x17, chip_id=0x8012,
                display_name='Apple T2 MacBookAir8,1 (j140k)'),
    IRecvDevice(product_type='iBridge2,10', hardware_model='j213ap', board_id=0x18, chip_id=0x8012,
                display_name='Apple T2 MacBookPro15,4 (j213)'),
    IRecvDevice(product_type='iBridge2,12', hardware_model='j140aap', board_id=0x37, chip_id=0x8012,
                display_name='Apple T2 MacBookAir8,2 (j140a)'),
    IRecvDevice(product_type='iBridge2,14', hardware_model='j152fap', board_id=0x3A, chip_id=0x8012,
                display_name='Apple T2 MacBookPro16,1 (j152f)'),
    IRecvDevice(product_type='iBridge2,15', hardware_model='j230kap', board_id=0x3F, chip_id=0x8012,
                display_name='Apple T2 MacBookAir9,1 (j230k)'),
    IRecvDevice(product_type='iBridge2,16', hardware_model='j214kap', board_id=0x3E, chip_id=0x8012,
                display_name='Apple T2 MacBookPro16,2 (j214k)'),
    IRecvDevice(product_type='iBridge2,19', hardware_model='j185ap', board_id=0x22, chip_id=0x8012,
                display_name='Apple T2 iMac20,1 (j185)'),
    IRecvDevice(product_type='iBridge2,20', hardware_model='j185fap', board_id=0x23, chip_id=0x8012,
                display_name='Apple T2 iMac20,2 (j185f)'),
    IRecvDevice(product_type='iBridge2,21', hardware_model='j223ap', board_id=0x3B, chip_id=0x8012,
                display_name='Apple T2 MacBookPro16,3 (j223)'),
    IRecvDevice(product_type='iBridge2,22', hardware_model='j215ap', board_id=0x38, chip_id=0x8012,
                display_name='Apple T2 MacBookPro16,4 (j215)'),
    # Apple Displays
    IRecvDevice(product_type='AppleDisplay2,1', hardware_model='j327ap', board_id=0x22, chip_id=0x8030,
                display_name='Studio Display'),
)
