import enclosing_circle

def mean_pos(user,pri_users,grid_points):
    tot_sum=0
    weight_sum = 0
    for i in user:
        tot_sum=tot_sum+i['coord']*i['upi']
        weight_sum = weight_sum + i['upi']
    dyn_pt= tot_sum/weight_sum
    leastDist = enclosing_circle.dist(grid_points[0]["pt"],dyn_pt)
    finalpt = grid_points[0]["id"]
    for i in grid_points :
        dt = enclosing_circle.dist(dyn_pt,i["pt"])
        if dt<leastDist:
            leastDist=dt
            finalpt=i["id"]
    return finalpt
    
