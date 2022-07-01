import os


def test_temporary_files():
    base_dir = '/app/solutions'
    temp_dirs = ['.idea']
    check_dirs = []

    for solution in sorted(next(os.walk(base_dir))[1]):
        for temp_dir in temp_dirs:
            check_dirs.append(os.path.join(base_dir, solution, temp_dir))

    assert all([not os.path.isdir(check_dir) for check_dir in check_dirs]), \
        'You seem to have committed some temporary files. See Canvas for the fix.'
