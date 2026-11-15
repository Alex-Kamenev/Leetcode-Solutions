"""Compile each independent Java answer and check negative values and duplicates."""
import argparse
import os
from pathlib import Path
import shutil
import subprocess
import tempfile

parser = argparse.ArgumentParser()
parser.add_argument("--jdk-dir", type=Path)
args = parser.parse_args()
suffix = ".exe" if os.name == "nt" else ""
javac = str(args.jdk_dir / "bin" / ("javac" + suffix)) if args.jdk_dir else shutil.which("javac")
java = str(args.jdk_dir / "bin" / ("java" + suffix)) if args.jdk_dir else shutil.which("java")
if not javac or not java:
    raise SystemExit("Install a JDK and add its bin directory to PATH, or pass --jdk-dir.")

source = (Path(__file__).resolve().parents[1] / "Kth largest").read_text()
answers = source.split("SORT and THEN return:")
runner = '''
class Regression {
    public static void main(String[] args) {
        Solution solution = new Solution();
        if (solution.findKthLargest(new int[]{-5, -2, -8}, 2) != -5) throw new AssertionError("Negative values");
        if (solution.findKthLargest(new int[]{3, 2, 3, 1, 2, 4, 5, 5, 6}, 4) != 4) throw new AssertionError("Duplicates");
        if (solution.findKthLargest(new int[]{Integer.MIN_VALUE}, 1) != Integer.MIN_VALUE) throw new AssertionError("Minimum integer");
        try { solution.findKthLargest(new int[]{1}, 0); throw new AssertionError("Invalid k"); }
        catch (IllegalArgumentException expected) { }
    }
}
'''
for index, answer in enumerate(answers, 1):
    answer = answer[answer.index("class Solution"):].strip()
    with tempfile.TemporaryDirectory(prefix="kth-largest-") as directory:
        folder = Path(directory)
        (folder / "Solution.java").write_text(answer)
        (folder / "Regression.java").write_text(runner)
        subprocess.run([javac, "Solution.java", "Regression.java"], cwd=folder, check=True)
        subprocess.run([java, "-cp", ".", "Regression"], cwd=folder, check=True)
    print(f"Solution {index}: passed")
