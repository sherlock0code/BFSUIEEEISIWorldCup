# *- coding:utf-8 -*-

"""
 Data clean utils
"""
import sys

import file_utils
from file_directions import working_file_url, clean_data_temp_file_url

reload(sys)
sys.setdefaultencoding('utf-8')


def merge_rows(file_name, keys=None, file_url=working_file_url, dst_file_url=clean_data_temp_file_url):
    """
    merge a table's rows with the same unique keys.
    :param file_name:
    :param keys:
    :param file_url:
    :param dst_file_url: which file folder should store the result
    :return:
    """
    # origin_df = file_utils.read_file(working_file_url + file_name)
    # data_frame = origin_df
    # data_frames = [data_frame]
    #
    # str_keys = []
    # for index in range(1, len(origin_df)):
    #     anchor_row = origin_df[index - 1:index]
    #
    #     temp_df = origin_df[index:]
    #     for key in keys:
    #         if index == 1:
    #             str_keys.append(key.encode('utf-8'))
    #         temp_df = temp_df.loc[temp_df[key.encode('utf-8')] == anchor_row.loc[index-1, key.encode('utf-8')]]
    #
    #     duplicated_num = len(temp_df)
    #     for j in range(0, duplicated_num):
    #         data_frames[0] = data_frames[0].drop(index=index)
    #
    #     for frame_nums in range(1, duplicated_num + 1):
    #         if len(data_frames) > frame_nums:
    #             data_frames[frame_nums] = data_frames[frame_nums].append(temp_df[frame_nums - 1: frame_nums])
    #         else:
    #             new_df = temp_df[frame_nums - 1: frame_nums]
    #             data_frames.append(new_df)
    #
    #     index += duplicated_num
    #
    # data_frame = data_frames[0]
    # for df in data_frames:
    #     data_frame = pandas.merge(data_frame, df, how='left', on=origin_df.columns.tolist())

    data_frame = file_utils.read_file_to_df(file_url, file_name)
    data_frame = data_frame.drop_duplicates()

    file_utils.write_file(data_frame, file_utils.check_file_url(dst_file_url), file_name,
                          sheet_name='Sheet', index=False)

    return


def drop_rows_too_many_empty(file_name, columns, thresh=2, file_url=clean_data_temp_file_url,
                             dst_file_url=clean_data_temp_file_url):
    """
    drop rows that too many values are empty.
    :param file_name:
    :param columns: the columns we need to check if it is empty
    :param thresh: how many empty is 'too many'
    :param file_url: input file url
    :param dst_file_url: where to store the result
    :return:
    """
    data_frame = file_utils.read_file_to_df(file_url, file_name)
    data_frame = data_frame.dropna(subset=columns, thresh=thresh)

    file_utils.write_file(data_frame, file_utils.check_file_url(dst_file_url), file_name,
                          sheet_name='Sheet', index=False)
    return
