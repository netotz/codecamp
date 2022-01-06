using System.Text;
using BenchmarkDotNet.Attributes;

namespace PlusMinusConversion;

public class SolutionsBenchmark {
    public string Input { get; }

    public SolutionsBenchmark() {
        Input = GenerateRandomInput(100_000);
    }

    public string GenerateRandomInput(int wordsCount) {
        var random = new Random();
        var input = new StringBuilder();
    
        while (wordsCount > 0) {
            input.Append(random.Next() % 2 == 0 ? "plus" : "minus");
            wordsCount--;
        }
    
        return input.ToString();
    }

    /// Submitted solution
    [Benchmark]
    public string SolveReplace() {
        return Input.Replace("plus", "+").Replace("minus", "-");
    }

    /// Refactored solution
    [Benchmark]
    public string SolveBuild() {
        var stringBuilder = new StringBuilder();
        for (int i = 0; i < Input.Length; i++) {
            if (Input[i] == 'p') {
                stringBuilder.Append('+');
                i += 4;
            }
            else if (Input[i] == 'm') {
                stringBuilder.Append('-');
                i += 5;
            }
        }
        return stringBuilder.ToString();
    }
}