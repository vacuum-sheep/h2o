Under llama7b, test bechmark(measuring in ) of openboookqa under 0.01, 0.2, 0.4, 0.6, 0.8, 1.0 kv cache budget with full,local, h2o strategy.

based on run_lm_eval_harness.py,  sample_size: all samples

flow:
dataGeneration.sh
run_xxx_batch.sh
eval_performance.sh

1. full cache
{
  "results": {
    "openbookqa": {
      "acc": 0.448,
      "acc_stderr": 0.02226169729227014,
      "acc_norm": 0.49,
      "acc_norm_stderr": 0.022378596989230774
    }
  },
  "versions": {
    "openbookqa": 0
  }
}

2. h2o
0.01
{
  "results": {
    "openbookqa": {
      "acc": 0.234,
      "acc_stderr": 0.018952741564893686,
      "acc_norm": 0.324,
      "acc_norm_stderr": 0.020950557312477455
    }
  },
  "versions": {
    "openbookqa": 0
  }
}


0.2
{
  "results": {
    "openbookqa": {
      "acc": 0.446,
      "acc_stderr": 0.022252153078595897,
      "acc_norm": 0.49,
      "acc_norm_stderr": 0.022378596989230774
    }
  },
  "versions": {
    "openbookqa": 0
  }
}


0.4
{
  "results": {
    "openbookqa": {
      "acc": 0.456,
      "acc_stderr": 0.02229623834840705,
      "acc_norm": 0.488,
      "acc_norm_stderr": 0.02237662679792717
    }
  },
  "versions": {
    "openbookqa": 0
  }
}


0.6
{
  "results": {
    "openbookqa": {
      "acc": 0.456,
      "acc_stderr": 0.02229623834840705,
      "acc_norm": 0.488,
      "acc_norm_stderr": 0.02237662679792717
    }
  },
  "versions": {
    "openbookqa": 0
  }
}



0.8
{
  "results": {
    "openbookqa": {
      "acc": 0.456,
      "acc_stderr": 0.02229623834840705,
      "acc_norm": 0.488,
      "acc_norm_stderr": 0.02237662679792717
    }
  },
  "versions": {
    "openbookqa": 0
  }
}


1.0
{
  "results": {
    "openbookqa": {
      "acc": 0.444,
      "acc_stderr": 0.022242244375731017,
      "acc_norm": 0.488,
      "acc_norm_stderr": 0.02237662679792717
    }
  },
  "versions": {
    "openbookqa": 0
  }
}


3. local
0.01
{
  "results": {
    "openbookqa": {
      "acc": 0.236,
      "acc_stderr": 0.01900869962208472,
      "acc_norm": 0.336,
      "acc_norm_stderr": 0.021144791425048846
    }
  },
  "versions": {
    "openbookqa": 0
  }
}


0.2
{
  "results": {
    "openbookqa": {
      "acc": 0.284,
      "acc_stderr": 0.020186703693570857,
      "acc_norm": 0.406,
      "acc_norm_stderr": 0.021983962090086337
    }
  },
  "versions": {
    "openbookqa": 0
  }
}


0.4
{
  "results": {
    "openbookqa": {
      "acc": 0.248,
      "acc_stderr": 0.019332342821239107,
      "acc_norm": 0.368,
      "acc_norm_stderr": 0.02158898256835354
    }
  },
  "versions": {
    "openbookqa": 0
  }
}


0.6
{
  "results": {
    "openbookqa": {
      "acc": 0.266,
      "acc_stderr": 0.01978055967565549,
      "acc_norm": 0.374,
      "acc_norm_stderr": 0.02166071034720448
    }
  },
  "versions": {
    "openbookqa": 0
  }
}


0.8
{
  "results": {
    "openbookqa": {
      "acc": 0.316,
      "acc_stderr": 0.020812359515855857,
      "acc_norm": 0.382,
      "acc_norm_stderr": 0.02175082059125084
    }
  },
  "versions": {
    "openbookqa": 0
  }
}


1.0
{
  "results": {
    "openbookqa": {
      "acc": 0.448,
      "acc_stderr": 0.02226169729227014,
      "acc_norm": 0.49,
      "acc_norm_stderr": 0.022378596989230774
    }
  },
  "versions": {
    "openbookqa": 0
  }
}
