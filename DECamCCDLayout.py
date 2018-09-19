#!/usr/bin/env python
    
def row_info(row_num):
    return [(2,True),(2,False),(3,True), (3,False), (3,False), (4,True), (4,True), (3,False), (3,False), (3,True), (2,False), (2,True)][row_num]

def draw_one_ccd(row_num, ccd_num, rowHasStub):
    
    scale = 6.0 / 4096.0
    
    ulx = (((ccd_num - (0.5 if ccd_num > 0 and rowHasStub else 0.0)) * 4096.0) + ((ccd_num + (0.0 if rowHasStub else 0.5)) * 153.0)) * scale
    uly = (1200.0 + row_num * (2048.0 + 201.0)) * scale
    
    brx = ulx + (2048.0 if (ccd_num == 0 and rowHasStub) else 4096.0) * scale
    bry = uly + 2048.0 * scale
    
    
    print "\draw  [fill=bluegray,bluegray] (" + ("%.3f"%ulx) + "," + ("%.3f"%uly) + ") rectangle (" + ("%.3f"%brx) + "," + ("%.3f"%bry) + ") node {};"
    
def do():
    for row_num in range(12):
        (num_ccds_in_row, rowHasStub) = row_info(row_num)
        for ccd_num in range(num_ccds_in_row):
            draw_one_ccd(row_num, ccd_num, rowHasStub)
    
    
        
if __name__ == '__main__':

    do()
    
    
    
