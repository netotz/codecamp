using System.Text;
using BenchmarkDotNet.Attributes;

namespace PlusMinusConversion;

public class SolutionsBenchmark {
    public const string plus = nameof(plus);
    public const string minus = nameof(minus);
    [ParamsSource(nameof(RandomInputs))]
    public string Input { get; set; }
    public IEnumerable<string> RandomInputs => Enumerable.Range(2, 5)
            .Select(n => {
                var wordsCount = (int)Math.Pow(10, n);
                return GenerateRandomInput(wordsCount);
            });

    public string GenerateRandomInput(int wordsCount) {
        var random = new Random();
        var input = new StringBuilder();
    
        while (wordsCount > 0) {
            input.Append(random.Next() % 2 == 0 ? plus : minus);
            wordsCount--;
        }
    
        return input.ToString();
    }

    /// <summary>
    /// Submitted solution
    /// </summary>
    [Benchmark]
    public string SolveReplace() {
        return Input.Replace(plus, "+").Replace(minus, "-");
    }

    /// <summary>
    /// Refactored solution
    /// </summary>
    [Benchmark]
    public string SolveBuild() {
        var stringBuilder = new StringBuilder();
        for (int i = 0; i < Input.Length; i++) {
            if (Input[i] == plus[0]) {
                stringBuilder.Append('+');
                i += plus.Length;
            }
            else if (Input[i] == minus[0]) {
                stringBuilder.Append('-');
                i += minus.Length;
            }
        }
        return stringBuilder.ToString();
    }
}