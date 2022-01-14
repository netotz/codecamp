using BenchmarkDotNet.Running;
using PlusMinusConversion;

var benchmark = BenchmarkRunner.Run<SolverBenchmark>();