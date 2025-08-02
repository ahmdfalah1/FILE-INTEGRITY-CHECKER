import hashlib
import argparse

def compute_hash(file_path, algorithm='sha256'):
    """Compute hash value of the file using the specified algorithm."""
    hash_func = getattr(hashlib, algorithm)()
    with open(file_path, 'rb') as f:
        while chunk := f.read(4096):
            hash_func.update(chunk)
    return hash_func.hexdigest()

def save_hash(file_path, hash_value, algorithm):
    """Save the algorithm and hash to a .hash file."""
    with open(file_path + '.hash', 'w') as f:
        f.write(f"{algorithm} {hash_value}")

def load_hash(file_path):
    """Load the algorithm and saved hash value."""
    try:
        with open(file_path + '.hash', 'r') as f:
            content = f.read().strip().split()
            if len(content) != 2:
                return None, None
            return content[0], content[1]  # algorithm, hash
    except FileNotFoundError:
        return None, None

def verify_file(file_path):
    """Compare current hash with saved hash using stored algorithm."""
    saved_algorithm, saved_hash = load_hash(file_path)
    if saved_algorithm is None:
        print(f"No hash found. Run without '--verify' to create one.")
        return

    current_hash = compute_hash(file_path, saved_algorithm)

    if current_hash == saved_hash:
        print("✅ File integrity verified. No changes detected.")
    else:
        print("❌ File has been modified or corrupted!")
        print(f"Expected ({saved_algorithm}): {saved_hash}")
        print(f"Current  ({saved_algorithm}): {current_hash}")

def main():
    parser = argparse.ArgumentParser(description="File Integrity Checker")
    parser.add_argument("file", help="File to check")
    parser.add_argument("--verify", action="store_true", help="Verify file integrity")
    parser.add_argument("--algorithm", default="sha256", help="Hash algorithm (default: sha256)")

    args = parser.parse_args()

    if args.verify:
        verify_file(args.file)
    else:
        hash_val = compute_hash(args.file, args.algorithm)
        save_hash(args.file, hash_val, args.algorithm)
        print(f"{args.algorithm.upper()} hash saved: {hash_val}")

if __name__ == "__main__":
    main()
