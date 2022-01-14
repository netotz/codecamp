using Xunit;

namespace PlusMinusConversion.Tests;

public class SolverBenchmarkTests
{

    [Theory]
    [InlineData("plus", "+")]
    [InlineData("minus", "-")]
    [InlineData("plusminus", "+-")]
    [InlineData("minusplusminusplus", "-+-+")]
    public void SolveReplace_AnyInput_ReplacesAllOccurences(string input, string answer)
    {
        var actual = Solver.SolveReplace(input);
        Assert.Equal(answer, actual);
    }
}