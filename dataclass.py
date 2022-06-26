from dataclasses import dataclass

@dataclass
class Row:
    iat: int
    st: int
    arrival: int
    sstart: int
    send: int
    #members for performance metrics
    waiting: int
    qlen: int


r = Row
r.arrival = 15
r.sstart = 21
r.waiting = r.sstart - r.arrival

print(r.waiting)

sim_table = []
sim_table.append(r)
print(sim_table[0].arrival)