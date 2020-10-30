import perfplot
from networkx.generators import random_regular_graph
from BioSpecGT.biospecgt.graph.generator import k_regular_graph

perfplot.show(
    setup=lambda n: n,  # or setup=numpy.random.rand
    kernels=[
        lambda a: random_regular_graph(d=a // 2, n=a),
        lambda a: k_regular_graph(n=a, k=a // 2),
    ],
    labels=["networkx", "biospecgt"],
    n_range=[k for k in range(100, 120, 2)],
    xlabel="Number of nodes",
    # logx=False,
    # logy=False,
    # More optional arguments with their default values:
    # logx="auto",  # set to True or False to force scaling
    # logy="auto",
    equality_check=None,  # set to None to disable "correctness" assertion
    show_progress=True,
    # target_time_per_measurement=1.0,
    # time_unit="s",  # set to one of ("auto", "s", "ms", "us", or "ns") to force plot units
    # relative_to=1,  # plot the timings relative to one of the measurements
    # flops=lambda n: 3*n,  # FLOPS plots
)
