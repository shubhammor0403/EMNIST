import tensorflow as tf
from tensorflow.python.framework.graph_util import convert_variables_to_constants


def freeze_graph(session, keep_var_names = None, output_names = None, clear_devices=True):
    graph = session.graph
    with graph.as_default():
        fvr = list(set(v.op.name for v in tf.global_variables()).difference(keep_var_names or []))
        output_names = output_names or []
        output_names += [v.op.name for v in tf.global_variables()]
        igf = graph.as_graph_def()
        if clear_devices:
            for node in igf.node:
                node.device=''
        frozen_graph= convert_variables_to_constants(session, igf, output_names, fvr)
        return frozen_graph

