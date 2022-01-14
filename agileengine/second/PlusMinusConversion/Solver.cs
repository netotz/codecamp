using System.Text;

namespace PlusMinusConversion;

public class Solver {
    public const string plus = nameof(plus);
    public const string minus = nameof(minus);

    /// <summary>
    /// Submitted solution
    /// </summary>
    public static string SolveReplace(string input) {
        return input.Replace(plus, "+").Replace(minus, "-");
    }

    /// <summary>
    /// Refactored solution
    /// </summary>
    public static string SolveBuild(string input) {
        var stringBuilder = new StringBuilder();
        for (int i = 0; i < input.Length; i++) {
            if (input[i] == plus[0]) {
                stringBuilder.Append('+');
                i += plus.Length;
            }
            else if (input[i] == minus[0]) {
                stringBuilder.Append('-');
                i += minus.Length;
            }
        }
        return stringBuilder.ToString();
    }
}