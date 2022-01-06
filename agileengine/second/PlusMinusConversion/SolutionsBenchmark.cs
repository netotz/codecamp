using System.Text;
using BenchmarkDotNet.Attributes;

namespace PlusMinusConversion;

public class SolutionsBenchmark {
    [Params(10, 100, 1000, 10_000, 100_000, 1_000_000)]
    public int WordsCount { get; set; }
    public string Input { get; }

    public SolutionsBenchmark() {
        Input = GenerateRandomInput(WordsCount);
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
        var capacity = Input.Length / 4;
        var stringBuilder = new StringBuilder(capacity, capacity);
        foreach (var character in Input) {
            if (character == 'p') {
                stringBuilder.Append('+');
            }
            else if (character == 'm') {
                stringBuilder.Append('-');
            }
        }
        return stringBuilder.ToString();
    }
}