from collections import namedtuple
Row = namedtuple("Row", "customer iat st arrival_time service time service_start service_end waiting_time queue_length")

r = Row
r.arrival = 15
r.sstart = 21
r.waiting = r.sstart - r.arrival

print(r.waiting)

sim_table = []
sim_table.append(r)
print(sim_table[0].arrival)


