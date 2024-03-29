using System.Text;
using BenchmarkDotNet.Attributes;

namespace PlusMinusConversion;

public class SolverBenchmark {
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

    [Benchmark]
    public void SolveReplace() {
        Solver.SolveReplace(Input);
    }

    [Benchmark]
    public void SolveBuild() {
        Solver.SolveBuild(Input);
    }
}