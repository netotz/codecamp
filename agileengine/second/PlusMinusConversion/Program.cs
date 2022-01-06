using BenchmarkDotNet.Running;
using PlusMinusConversion;

var benchmark = BenchmarkRunner.Run<SolutionsBenchmark>();
Console.WriteLine(benchmark);