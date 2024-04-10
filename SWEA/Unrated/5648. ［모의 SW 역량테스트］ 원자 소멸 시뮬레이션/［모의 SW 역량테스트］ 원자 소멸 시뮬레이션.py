from collections import Counter

def get_total_energy(n, atoms):
    answer = 0
    '''
    0: 상
    1: 하
    2: 좌
    3: 우
    '''
    dx = [0, 0, -0.5, 0.5]
    dy = [0.5, -0.5, 0, 0]

    # 최대 1000초 동안 이동 후 stop
    for time in range(0, 4000):
        atom_loc = []
        # move atom
        for i in range(len(atoms)):
            atoms[i][0] += dx[atoms[i][2]]
            atoms[i][1] += dy[atoms[i][2]]
            if -1000 <= atoms[i][0] <= 1000 and -1000 <= atoms[i][1] <= 1000:
                atom_loc.append((atoms[i][0], atoms[i][1]))

        # 충돌하는 원자 얻기
        counter = Counter(atom_loc)
        for i in counter:
            if counter[i] >= 2:
                crash_atoms = list(filter(lambda x: [x[0], x[1]]==list(i), atoms))
                for crash_atom in crash_atoms:
                    answer += crash_atom[3]
                    atoms.remove(crash_atom)

        if len(atoms) <= 1: break
    return answer


if __name__ == "__main__":
    # input
    t = int(input())

    for testcase in range(1, t+1):
        n = int(input())
        atoms = []
        for _ in range(n):
            atoms.append(list(map(int, input().split())))
        
        # get total energy
        total_energy = get_total_energy(n, atoms)
        print(f'#{testcase} {total_energy}')
